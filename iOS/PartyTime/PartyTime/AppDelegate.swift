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
        
        
//        let serverAddress = "172.20.10.5"
//        print("serverAddress: \(serverAddress)")
        
        let serverAddress = "192.168.2.14"
        UserDefaults.standard.set(serverAddress, forKey: "serverAddress")
//        let defaults = UserDefaults.standard
        
        var urlComponents = URLComponents()
        urlComponents.scheme = "http"
        urlComponents.host = serverAddress
        urlComponents.path = "/api/pos/allbeacons"
        urlComponents.port = 5000

//        guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
        
//        defaults.set(url, forKey: "serverAddress")
//        defaults.set(serverAddress, forKey: "serverAddress")
        
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
        for region in regions{
            locationManager.stopRangingBeacons(in: region)
        }
    }
    
    // from this line the functions was added by me
    
    
    
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
        //        beaconsList = getBeaconList()
        while UserDefaults.standard.string(forKey: "username")==nil {
            sleep(1)
            print("sto aspettando l'username")
        }
        
        print("chiamo getBeaconList() da startBeaconsScan")
        getBeaconList(){ (ret) in
            
            // [Beacon] is the value returned from the function!
            
            print("sono nella funzione locationManager(didChangeAuth)")
            print("questi sono i beacon che ho ottenuto:")
            for b in (ret){
                print(b.toPrint())
            }
            self.beaconsList = ret
            self.rangeBeacons(bList: ret)
            
            
        }
        
        //                rangeBeacons()
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
        print("entrato in getBeaconList()")
        
//        let url = URL(string: "http://192.168.2.14:5000/api/pos/allbeacons")
        
        let serverAddress = UserDefaults.standard.string(forKey: "serverAddress")
        
        var urlComponents = URLComponents()
        urlComponents.scheme = "http"
        urlComponents.host = serverAddress
        urlComponents.path = "/api/pos/allbeacons"
        urlComponents.port = 5000

        guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
//        let url = UserDefaults.standard.url(forKey: "serverAddress")
        print("printo l'url")
        print(url.absoluteString)
        let task = URLSession.shared.dataTask(with: url) {(data, response, error) in
            //            print("sono all'1")
            guard error == nil else { fatalError("returning error: \(error.debugDescription)") }
            //            print("sono all'2")
            
            //            guard let content = data else { fatalError("not returning data") }
            //            print("sono all'3")
            
            
            guard let json = try? JSONDecoder().decode(restBeaconList.self, from: data!) else {
                print("Error: Couldn't decode data into restBeaconList")
                return
            }
            //            guard let json = (try? JSONSerialization.jsonObject(with: content, options: JSONSerialization.ReadingOptions.mutableContainers)) as? [String: Any] else { fatalError("Not containing JSON") }
            //            print("sono all'4")
            
            DispatchQueue.main.async {
                var beacons = [Beacon]()
                for e in json.beacons {
                    //                    self.beaconsList.append(Beacon(room: e.room, uuid: e.uuid, minor: e.minor, major: e.major))
                    //                    print(e.uuid, e.room)
                    beacons.append(Beacon(room: e.room, uuid: e.uuid, minor: e.minor, major: e.major))
                    
                }
                
                //                print("sono all'5")
                returnCompletion(beacons as [Beacon])
                
                //                for b in self.beaconsList{
                //                    print(b.toPrint())
                //                }
                //                print()
            }
            
            
            
        }
        //        print("sono prima del resume")
        
        task.resume()
        
    }
    
    
    func rangeBeacons(bList: [Beacon]){
        //        let uuid = UUID(uuidString: "3e1d7817-4eac-4b27-b809-deee2f246c46")
        //        let uuid = UUID(uuidString: "8492E75F-4FD6-469D-B132-043FE94921D8")
        //        let major:CLBeaconMajorValue = 1
        //        let minor:CLBeaconMinorValue = 2
        //        let identifier = "myBeacon"
        //        let region = CLBeaconRegion(proximityUUID: uuid!, major: major, minor: minor, identifier: identifier)
        //        var region = [CLBeaconRegion]()
        
        print("Sono nella funzione rangeBeacons")
        
        
        //        let newRegion = CLBeaconRegion(proximityUUID: bList[0].bUUID, identifier: bList[0].room)
        
        // creo una lista di beaconRegion, una per beacon
        
        for b in bList{
            regions.append(CLBeaconRegion(proximityUUID: b.bUUID, major: b.bMajor, minor: b.bMinor, identifier: b.room))
        }
        
        //        var i = 0
        
        //        for r in region{
        //            print("Region\(i) di identificativo:\(r.identifier)")
        //            i += 1
        //            r.notifyOnEntry = true
        //            r.notifyEntryStateOnDisplay = true
        //            r.notifyOnExit = true
        //            locationManager.startRangingBeacons(in: r)
        //            locationManager.startMonitoring(for: r)
        //        }
        
        for region in regions{
            region.notifyOnEntry = true
            region.notifyEntryStateOnDisplay = true
            region.notifyOnExit = true
            //locationManager.startRangingBeacons(in: region)
            locationManager.startMonitoring(for: region)
        }
        //        print("Region\(i) di identificativo:\(newRegion.identifier)")
        //        i += 1
        
        
        
        //        region.notifyOnEntry = true
        //        region.notifyEntryStateOnDisplay = true
        //        region.notifyOnExit = true
        //
        //        locationManager.startRangingBeacons(in: region)
        //        locationManager.startMonitoring(for: region)
    }
    
    //    func locationManager(_ manager: CLLocationManager, didRangeBeacons beacons: [CLBeacon], in region: CLBeaconRegion) {
    //        print(beacons)
    //    }
    
    func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion) {
        
        let beaconRegion = region as! CLBeaconRegion
        
        print("Ho rilevaro in INGRESSO: \(beaconRegion.identifier)")
        
        registerPosition(region: beaconRegion)
        
        //        let content = UNMutableNotificationContent()
        //        content.title = "entered"
        //        content.body = "\(beaconRegion.identifier)"
        //        content.sound = .default()
        //        let request = UNNotificationRequest(identifier: "partyTime", content: content, trigger: nil)
        //        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
    func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion) {
        let beaconRegion = region as! CLBeaconRegion
        print("Ho rilevaro in USCITA: \(beaconRegion.identifier)")
        //        let content = UNMutableNotificationContent()
        //        content.title = "leave"
        //        content.body = "\(beaconRegion.identifier)"
        //        content.sound = .default()
        //        let request = UNNotificationRequest(identifier: "partyTime", content: content, trigger: nil)
        //        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
}


//let defaults = UserDefaults.standard
//        let username = defaults.string(forKey: "username")
//        print("Ho trovato l'username: \(username ?? "none")")
//        print("entrato nel createUser")
//        let myPost = Post(userId: 1, id: 1, title: "Hello World", body: "How are you all today?")


//let pref1 = defaults.string(forKey: "pref1")
//let pref2 = defaults.string(forKey: "pref2")
//let pref3 = defaults.string(forKey: "pref3")

//        print("prefs: \(pref1 ?? "nope") \(pref2 ?? "nope") \(pref3 ?? "nope")")


struct Post: Codable {
    let beacon: String
    let major: String
    let minor: String
    let username: String
}

func registerPosition(region: CLBeaconRegion){
    
//    let defaults = UserDefaults.standard
//    let username = defaults.string(forKey: "username")
    let username = UserDefaults.standard.string(forKey: "username")
    
    let myPostReq = Post(beacon: region.proximityUUID.uuidString, major: (region.major?.stringValue)!, minor: (region.minor?.stringValue)!, username: username!)
    print("beacon \(myPostReq.beacon) M \(myPostReq.major) m\(myPostReq.minor) user\(myPostReq.username)")
    
    submitPost(post: myPostReq) { (error) in
        if let error = error {
            //                print("non funge cazzo")
            fatalError(error.localizedDescription)
        }
    }
}


func submitPost(post: Post, completion:((Error?) -> Void)?) {
    
//    let username = UserDefaults.standard.string(forKey: "username")
    
    let serverAddress = UserDefaults.standard.string(forKey: "serverAddress")
    var urlComponents = URLComponents()
    urlComponents.scheme = "http"
    urlComponents.host = serverAddress
    urlComponents.port = 5000
    urlComponents.path = "/api/pos/update"
    guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
    
    //
    
    //    let url = URL(string: "http://192.168.2.14:5000/api/users/\(username ?? "non funge")")
    //
//    let url = UserDefaults.standard.url(forKey: "serverAddress")
    
    // Specify this request as being a POST method
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
        //            print("jsonData: ", String(data: request.httpBody!, encoding: .utf8) ?? "no body data")
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
        
        // APIs usually respond with the data you just sent in your POST request
        //            if let data = responseData, let utf8Representation = String(data: data, encoding: .utf8) {
        //                print("response: ", utf8Representation)
        //            } else {
        //                print("no readable data received in response")
        //            }
    }
    task.resume()
}



