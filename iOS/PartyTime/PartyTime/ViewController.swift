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

        if UserDefaults.standard.string(forKey: "username") != nil{
            let storyboard = UIStoryboard(name: "Main", bundle: nil)
            let controller = storyboard.instantiateViewController(withIdentifier: "lastViewController")
            self.present(controller, animated: false, completion: nil)
        }
        
        self.navigationController?.isNavigationBarHidden = true
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
        defaults.set(self.username, forKey: "username")
    }
    
    
    private func usernameAccepted(user: String) {

        self.username = user
        userInUseLabel.isHidden = true
        doneButton.isEnabled = true

    }
    
    private func usernameRejected(user: String) {

        userInUseLabel.isHidden = false
        doneButton.isEnabled = false

    }
    
    var responseStatus = 0
    
    @IBAction func saveUsername(_ sender: Any) {
        let user = textField.text
        self.username = user!
        
        let serverAddress = UserDefaults.standard.string(forKey: "serverAddress")
        
        var urlComponents = URLComponents()
        urlComponents.scheme = "http"
        urlComponents.host = serverAddress
        urlComponents.path = "/api/users/\(user ?? "")"
        urlComponents.port = 5000
        guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
        
        
        let task = URLSession.shared.downloadTask(with:url) { loc, resp, err in
            let status = (resp as! HTTPURLResponse).statusCode
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
    }
}

