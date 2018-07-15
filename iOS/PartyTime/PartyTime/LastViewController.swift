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
        let pref1 = defaults.string(forKey: "pref1")
        let pref2 = defaults.string(forKey: "pref2")
        let pref3 = defaults.string(forKey: "pref3")
        
        let myPost = Post(pref1: pref1!, pref2: pref2!, pref3: pref3!)
       
        submitPost(post: myPost) { (error) in
            if let error = error {
                fatalError(error.localizedDescription)
            }
            
        }
    }
    
    func submitPost(post: Post, completion:((Error?) -> Void)?) {
      let username = UserDefaults.standard.string(forKey: "username")
        let serverAddress = UserDefaults.standard.string(forKey: "serverAddress")
        
        var urlComponents = URLComponents()
        urlComponents.scheme = "http"
        urlComponents.host = serverAddress
        urlComponents.path = "/api/users/\(username ?? "cazzononfunziona")"
        urlComponents.port = 5000
        guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
        
        
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
    
    
    @IBAction func resetButton(_ sender: Any) {
        let defaults = UserDefaults.standard
        defaults.set(nil, forKey: "username")
        let firstViewController = self.storyboard?.instantiateViewController(withIdentifier: "firstView") as! ViewController
        self.navigationController?.pushViewController(firstViewController, animated: true)

    }
}
























