//
//  ViewController.swift
//  PartyTime
//
//  Created by jazz on 2/6/18.
//  Copyright © 2018 alessio-zamparelli. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var doneButton: UIButton!
    @IBOutlet weak var userInUseLabel: UILabel!
    
    var username = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        self.navigationController?.isNavigationBarHidden = true
        //        var db = DB()
        //        print("Sto printando quel che ho ricevuto:")
        //        db.getKindsOfMusicAndCount()
        //        db.storeKindsOfMusicAndCount()
//        doneButton.alpha = 0.4
        doneButton.isEnabled = false
        userInUseLabel.isHidden = true
        
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
        navigationItem.title = nil
        self.navigationController?.isNavigationBarHidden = false
        let defaults = UserDefaults.standard
//        print("Setting the username (\(self.username)) inside defaults")
        defaults.set(self.username, forKey: "username")
    }
    
    
    
    //    override func viewWillDisappear(_ animated: Bool) {
    //        super.viewWillDisappear(animated)
    //
    //        if (self.isMovingFromParentViewController) {
    //            self.navigationController?.isNavigationBarHidden = true
    //        }
    //    }
    
    private func usernameAccepted(user: String) {
//        print("Username accepted")
        self.username = user
//        doneButton.alpha = 1
//        doneButton.setTitle("Done", for: UIControlState.normal)
        
//       doneButton.backgroundColor = UIColor(red: 154.0, green: 154.0, blue: 154.0, alpha: 0.26)
//        doneButton.backgroundColor = UIColor(hue: 359, saturation: 0, brightness: 61, alpha: 0.26)
        userInUseLabel.isHidden = true
        doneButton.isEnabled = true
    }
    
    private func usernameRejected(user: String) {
//        print("Username rejected")
//        doneButton.alpha = 1
//        doneButton.backgroundColor = UIColor(red: 154.0, green: 154.0, blue: 154.0, alpha: 0.90)
//        doneButton.backgroundColor = UIColor(hue: 359, saturation: 0, brightness: 61, alpha: 0.60)
        
//        doneButton.setTitle("Username in Use", for: UIControlState.normal)
        userInUseLabel.isHidden = false
        doneButton.isEnabled = false
    }
    
    var responseStatus = 0
    
    @IBAction func saveUsername(_ sender: Any) {
        let user = textField.text
        self.username = user!
//        print("entrato nel saveUsername")
//        let url = URL(string: "http://192.168.2.14:5000/api/users/\(user ?? "")")
        
        let serverAddress = UserDefaults.standard.string(forKey: "serverAddress")
        
        var urlComponents = URLComponents()
        urlComponents.scheme = "http"
        urlComponents.host = serverAddress
        urlComponents.path = "/api/users/\(user ?? "")"
        
        guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
        
        let task = URLSession.shared.downloadTask(with:url) { loc, resp, err in
            let status = (resp as! HTTPURLResponse).statusCode
//            print("response status: \(status)")
            self.responseStatus = status
            DispatchQueue.main.async {
                switch self.responseStatus{
                case 202:
                    self.usernameRejected(user: self.username)
                case 204:
                    self.usernameAccepted(user: self.username)
                default:
                    fatalError("Response code unknow: \(self.responseStatus)")
                }
                
            }
            
        }
        task.resume()
        
        
//        let task = URLSession.shared.dataTask(with: url!) {(data, response, error) in
//
//            guard error == nil else { fatalError("returning error") }
//
//            guard let content = data else { fatalError("not returning data") }
//
//
//            guard let json = (try? JSONSerialization.jsonObject(with: content, options: JSONSerialization.ReadingOptions.mutableContainers)) as? [String: Any] else { fatalError("Not containing JSON") }
//
//            for e in json{
//                self.itemsList.append(Item(kind: e.key, numberOfSongs: (e.value as! Int)))
//            }
//
//            DispatchQueue.main.async {
//                self.tableOutlet.reloadData()
//            }
//
//        }
        
//        task.resume()
    }
    
}

