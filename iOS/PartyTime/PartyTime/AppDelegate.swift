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
        locationManager.delegate = self
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
    
    
    
    
    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
        getBeaconList()
        //        rangeBeacons()
        
    }
    
    
    
    func getBeaconList() {
        print("entrato in getBeaconList()")
        let url = URL(string: "http://192.168.2.14:5000/api/pos/allbeacons")
        let task = URLSession.shared.dataTask(with: url!) {(data, response, error) in
            print("sono all'1")
            guard error == nil else { fatalError("returning error") }
            print("sono all'2")
            
            guard let content = data else { fatalError("not returning data") }
            print("sono all'3")
            
            guard let json = (try? JSONSerialization.jsonObject(with: content, options: JSONSerialization.ReadingOptions.mutableContainers)) as? [String: Any] else { fatalError("Not containing JSON") }
            print("sono all'4")
            DispatchQueue.main.async {
                for e in json {
                    print(e.key, e.value)
                    print("sono all'5")
                }
            }
            
            
        }
        print("sono prima del resume")
        
        task.resume()
        
        
    }
    
    
    func rangeBeacons(){
        let uuid = UUID(uuidString: "3e1d7817-4eac-4b27-b809-deee2f246c46")
        //let uuid = UUID(uuidString: "8492E75F-4FD6-469D-B132-043FE94921D8")
        let major:CLBeaconMajorValue = 1
        let minor:CLBeaconMinorValue = 2
        let identifier = "myBeacon"
        let region = CLBeaconRegion(proximityUUID: uuid!, major: major, minor: minor, identifier: identifier)
        region.notifyOnEntry = true
        region.notifyEntryStateOnDisplay = true
        region.notifyOnExit = true
        locationManager.startRangingBeacons(in: region)
        locationManager.startMonitoring(for: region)
    }
    
    func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion) {
        let content = UNMutableNotificationContent()
        content.title = "Hello!!!"
        content.body = "You Are Back in the Office"
        content.sound = .default()
        let request = UNNotificationRequest(identifier: "SufalamTech", content: content, trigger: nil)
        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
    func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion) {
        let content = UNMutableNotificationContent()
        content.title = "Alert!!!"
        content.body = "You are Out of the Office"
        content.sound = .default()
        let request = UNNotificationRequest(identifier: "identifier", content: content, trigger: nil)
        UNUserNotificationCenter.current().add(request, withCompletionHandler: nil)
    }
    
}

