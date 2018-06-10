//
//  AppDelegate.swift
//  PartyTime
//
//  Created by jazz on 2/6/18.
//  Copyright © 2018 alessio-zamparelli. All rights reserved.
//

import UIKit
import CoreLocation
import UserNotifications

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, CLLocationManagerDelegate {
    
    var window: UIWindow?
    var locationManager:CLLocationManager = CLLocationManager()
    var beaconsList = [Beacon]()
    var regions = [CLBeaconRegion]()
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        
        print("Sono entrato nel delegate")
        locationManager.delegate = self
        
        print("sto per richiedere l'autorizzatione per la posizione")
        locationManager.requestAlwaysAuthorization()
        
        // se l'ho gia richiesta....
        if CLLocationManager.locationServicesEnabled(){
            startBeaconsScan()
        }
        
        // Request permission to send notifications
//        let center = UNUserNotificationCenter.current()
//        center.requestAuthorization(options:[.alert, .sound]) { (granted, error) in }
    
        let serverAddress = "192.168.2.14"
        UserDefaults.standard.set(serverAddress, forKey: "serverAddress")
        
        var urlComponents = URLComponents()
        urlComponents.scheme = "http"
        urlComponents.host = serverAddress
        urlComponents.path = "/api/pos/allbeacons"
        urlComponents.port = 5000

        
        return true
    }
    
    
    func applicationWillResignActive(_ application: UIApplication) {
        // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
        // Use this method to pause ongoing tasks, disable timers, and invalidate graphics rendering callbacks. Games should use this method to pause the game.
    }
    
    
    
    func applicationDidEnterBackground(_ application: UIApplication) {
        // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later.
        // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
        
    }
    
    func applicationWillEnterForeground(_ application: UIApplication) {
        // Called as part of the transition from the background to the active state; here you can undo many of the changes made on entering the background.
    }
    
    func applicationDidBecomeActive(_ application: UIApplication) {
        // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
    }
    
    func applicationWillTerminate(_ application: UIApplication) {
        // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
        // stoppo quando l'app viene chiusa completamente, anche dal background
        for region in regions{
            locationManager.stopRangingBeacons(in: region)
        }
    }
    
    // qui inizia il mio codice
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        
        startBeaconsScan()
        
    }
    
    func startBeaconsScan() {
        if !CLLocationManager.locationServicesEnabled(){
            for _ in 1...10 {
                print("Non ho la localizzazione")
            }
            fatalError("Non ho la localizzazione")
        }

        while UserDefaults.standard.string(forKey: "username")==nil {
            sleep(1)
        }
        
        getBeaconList(){ (ret) in
            
            // [Beacon] is the value returned from the function!
            
            self.beaconsList = ret
            self.rangeBeacons(bList: ret)

        }
    }
    
    struct restBeaconList: Decodable {
        
        let beacons : [restBeacon]
        
        enum CodingKeys : String, CodingKey {
            case beacons = "beacons"
        }
        
    }
    
    struct restBeacon: Decodable {
        let major: Int
        let minor: Int
        let room: String
        let uuid: String
    }
    
    func getBeaconList(returnCompletion: @escaping ([Beacon]) -> () ) {

        let serverAddress = UserDefaults.standard.string(forKey: "serverAddress")
        
        var urlComponents = URLComponents()
        urlComponents.scheme = "http"
        urlComponents.host = serverAddress
        urlComponents.path = "/api/pos/allbeacons"
        urlComponents.port = 5000

        guard let url = urlComponents.url else { fatalError("Could not create URL from components") }

        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in

            guard error == nil else { fatalError("returning error: \(error.debugDescription)") }

            guard let json = try? JSONDecoder().decode(restBeaconList.self, from: data!) else {
                print("Error: Couldn't decode data into restBeaconList")
                return
            }

            DispatchQueue.main.async {
                var beacons = [Beacon]()
                for e in json.beacons {
                    beacons.append(Beacon(room: e.room, uuid: e.uuid, minor: e.minor, major: e.major))
                }
                
                returnCompletion(beacons as [Beacon])
         
            }
        }
        
        task.resume()
    }
    
    
    func rangeBeacons(bList: [Beacon]){
      for b in bList{
            regions.append(CLBeaconRegion(proximityUUID: b.bUUID, major: b.bMajor, minor: b.bMinor, identifier: b.room))
        }
      
        for region in regions{
            region.notifyOnEntry = true
            region.notifyEntryStateOnDisplay = true
            region.notifyOnExit = true
            locationManager.startMonitoring(for: region)
        }
    }
  
    func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion) {
        
        let beaconRegion = region as! CLBeaconRegion
        
        print("Ho rilevaro in INGRESSO: \(beaconRegion.identifier)")
        
        registerPosition(region: beaconRegion)
     }
    
    func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion) {
        let beaconRegion = region as! CLBeaconRegion
        print("Ho rilevaro in USCITA: \(beaconRegion.identifier)")
     }
    
}

struct Post: Codable {
    let beacon: String
    let major: String
    let minor: String
    let username: String
}

func registerPosition(region: CLBeaconRegion){
    
    let username = UserDefaults.standard.string(forKey: "username")
    
    let myPostReq = Post(beacon: region.proximityUUID.uuidString, major: (region.major?.stringValue)!, minor: (region.minor?.stringValue)!, username: username!)
    
    submitPost(post: myPostReq) { (error) in
        if let error = error {
            fatalError(error.localizedDescription)
        }
    }
}


func submitPost(post: Post, completion:((Error?) -> Void)?) {
    
    let serverAddress = UserDefaults.standard.string(forKey: "serverAddress")
    var urlComponents = URLComponents()
    urlComponents.scheme = "http"
    urlComponents.host = serverAddress
    urlComponents.port = 5000
    urlComponents.path = "/api/pos/update"
    guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
 
    var request = URLRequest(url: url)
    request.httpMethod = "POST"
    // Make sure that we include headers specifying that our request's HTTP body
    // will be JSON encoded
    var headers = request.allHTTPHeaderFields ?? [:]
    headers["Content-Type"] = "application/json"
    request.allHTTPHeaderFields = headers
    
    // Now let's encode out Post struct into JSON data...
    let encoder = JSONEncoder()
    do {
        let jsonData = try encoder.encode(post)
        // ... and set our request's HTTP body
        request.httpBody = jsonData
    } catch {
        completion?(error)
    }
    
    // Create and run a URLSession data task with our JSON encoded POST request
    let config = URLSessionConfiguration.default
    let session = URLSession(configuration: config)
    let task = session.dataTask(with: request) { (responseData, response, responseError) in
        guard responseError == nil else {
            completion?(responseError!)
            return
        }

    }
    task.resume()
}



