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
    
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        // Override point for customization after application launch.
        
        print("Sono entrato nel delegate")
        locationManager.delegate = self
        
        print("sto per richiedere l'autorizzatione...")
        locationManager.requestAlwaysAuthorization()
        
        
        // Request permission to send notifications
        let center = UNUserNotificationCenter.current()
        center.requestAuthorization(options:[.alert, .sound]) { (granted, error) in }
        
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
    }
    
    // from this line the functions was added by me
    
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        //        beaconsList = getBeaconList()
        print("chiamo getBeaconList() da locationManager(didChangeAuthorization)")
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
        
        let url = URL(string: "http://192.168.2.14:5000/api/pos/allbeacons")
        let task = URLSession.shared.dataTask(with: url!) {(data, response, error) in
//            print("sono all'1")
            guard error == nil else { fatalError("returning error") }
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
        var region = [CLBeaconRegion]()
        
        print("Sono nella funzione rangeBeacons")
        
        var newRegion = CLBeaconRegion(proximityUUID: bList[0].bUUID, identifier: bList[0].room)
//        for b in bList{
//            region.append(CLBeaconRegion(proximityUUID: b.bUUID, major: b.bMajor, minor: b.bMinor, identifier: b.room))
//        }
        
        var i = 0
        
//        for r in region{
//            print("Region\(i) di identificativo:\(r.identifier)")
//            i += 1
//            r.notifyOnEntry = true
//            r.notifyEntryStateOnDisplay = true
//            r.notifyOnExit = true
//            locationManager.startRangingBeacons(in: r)
//            locationManager.startMonitoring(for: r)
//        }
        
        print("Region\(i) di identificativo:\(newRegion.identifier)")
        i += 1
        newRegion.notifyOnEntry = true
        newRegion.notifyEntryStateOnDisplay = true
        newRegion.notifyOnExit = true
        locationManager.startRangingBeacons(in: newRegion)
        locationManager.startMonitoring(for: newRegion)
        
        
        //        region.notifyOnEntry = true
        //        region.notifyEntryStateOnDisplay = true
        //        region.notifyOnExit = true
        //
        //        locationManager.startRangingBeacons(in: region)
        //        locationManager.startMonitoring(for: region)
    }
    
    func locationManager(_ manager: CLLocationManager, didRangeBeacons beacons: [CLBeacon], in region: CLBeaconRegion) {
        print(beacons)
    }
    
    func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion) {
        let beaconRegion = region as! CLBeaconRegion
        print("Ho rilevaro in INGRESSO: \(beaconRegion.identifier)")
        let content = UNMutableNotificationContent()
        content.title = "entered"
        content.body = "\(beaconRegion.identifier)"
        content.sound = .default()
        let request = UNNotificationRequest(identifier: "partyTime", content: content, trigger: nil)
        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
    func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion) {
        let beaconRegion = region as! CLBeaconRegion
        print("Ho rilevaro in USCITA: \(beaconRegion.identifier)")
        let content = UNMutableNotificationContent()
        content.title = "leave"
        content.body = "\(beaconRegion.identifier)"
        content.sound = .default()
        let request = UNNotificationRequest(identifier: "partyTime", content: content, trigger: nil)
        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
}

