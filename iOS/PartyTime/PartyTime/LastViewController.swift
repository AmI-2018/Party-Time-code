//
//  LastViewController.swift
//  PartyTime
//
//  Created by jazz on 4/6/18.
//  Copyright © 2018 alessio-zamparelli. All rights reserved.
//

import UIKit
import CoreLocation

class LastViewController: UIViewController{
    
    var selectedList = [Item]()
    var locationManager: CLLocationManager!
    
    @IBOutlet weak var distanceLabel: UILabel!
    @IBOutlet weak var beaconIdLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view.
        
        self.navigationController?.isNavigationBarHidden = true
        createUser()
//        locationManager = CLLocationManager()
//        locationManager.delegate = self
//        locationManager.requestAlwaysAuthorization()
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    /*
     // MARK: - Navigation
     
     // In a storyboard-based application, you will often want to do a little preparation before navigation
     override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
     // Get the new view controller using segue.destinationViewController.
     // Pass the selected object to the new view controller.
     }
     */
    
    struct Post: Codable {
        let pref1: String
        let pref2: String
        let pref3: String
    }
    
    func createUser() {
        let defaults = UserDefaults.standard
        let username = defaults.string(forKey: "username")
        print("Ho trovato l'username: \(username ?? "none")")
        print("entrato nel createUser")
        //        let myPost = Post(userId: 1, id: 1, title: "Hello World", body: "How are you all today?")
        
        
        let pref1 = defaults.string(forKey: "pref1")
        let pref2 = defaults.string(forKey: "pref2")
        let pref3 = defaults.string(forKey: "pref3")
        
        print("prefs: \(pref1 ?? "nope") \(pref2 ?? "nope") \(pref3 ?? "nope")")
        
        let myPost = Post(pref1: pref1!, pref2: pref2!, pref3: pref3!)
        
        print("myPost: \(myPost)")
        
        
        //        let url = URL(string: "http://192.168.0.22:5000/api/users/\(username)")
        submitPost(post: myPost) { (error) in
            if let error = error {
                print("POrcoDIO")
                fatalError(error.localizedDescription)
            }
            
        }
    }
    
    func submitPost(post: Post, completion:((Error?) -> Void)?) {
        //        var urlComponents = URLComponents()
        //        urlComponents.scheme = "http"
        //        urlComponents.host = "192.168.2.14:5000"
        //        urlComponents.path = "/api/users/\(username)"
        //        guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
        //
        let username = UserDefaults.standard.string(forKey: "username")
        let url = URL(string: "http://192.168.2.14:5000/api/users/\(username ?? "cazzononfunziona")")
        
        // Specify this request as being a POST method
        var request = URLRequest(url: url!)
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
            print("jsonData: ", String(data: request.httpBody!, encoding: .utf8) ?? "no body data")
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
            if let data = responseData, let utf8Representation = String(data: data, encoding: .utf8) {
                print("response: ", utf8Representation)
            } else {
                print("no readable data received in response")
            }
        }
        task.resume()
    }
//    
//    func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) {
//        if status == .authorizedAlways {
//            if CLLocationManager.isMonitoringAvailable(for: CLBeaconRegion.self) {
//                if CLLocationManager.isRangingAvailable() {
//                    startScanning()
//                }
//            }
//        }
//    }
//    
//    func startScanning() {
//        let uuid = UUID(uuidString: "5A4BCFCE-174E-4BAC-A814-092E77F6B7E5")!
//        let beaconRegion = CLBeaconRegion(proximityUUID: uuid, major: 123, minor: 456, identifier: "MyBeacon")
//        
//        locationManager.startMonitoring(for: beaconRegion)
//        locationManager.startRangingBeacons(in: beaconRegion)
//    }
//    
//    
//    
//    func locationManager(_ manager: CLLocationManager, didRangeBeacons beacons: [CLBeacon], in region: CLBeaconRegion) {
//        if beacons.count > 0 {
//            updateDistance(beacons[0].proximity)
//        } else {
//            updateDistance(.unknown)
//        }
//    }
//    
//    
//    
//    func updateDistance(_ distance: CLProximity) {
//        switch distance {
//        case .unknown:
//            distanceLabel.text = "boh"
//            
//            
//        case .far:
//            distanceLabel.text = "farfar away"
//            
//        case .near:
//            distanceLabel.text = "near"
//            
//        case .immediate:
//            distanceLabel.text = "in your pocket"
//        }
//    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
}



