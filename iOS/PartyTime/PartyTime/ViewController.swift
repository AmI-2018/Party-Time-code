//
//  ViewController.swift
//  PartyTime
//
//  Created by jazz on 2/6/18.
//  Copyright © 2018 alessio-zamparelli. All rights reserved.
//

import UIKit

class ViewController: UIViewController, NetServiceBrowserDelegate, NetServiceDelegate {
    
    @IBOutlet weak var textField: UITextField!
    @IBOutlet weak var doneButton: UIButton!
    @IBOutlet weak var userInUseLabel: UILabel!
    
    var username = ""
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        //        print("Sono nel viewController\nstampo l'username")
        //        print(UserDefaults.standard.string(forKey: "username") ?? "username non presente")
        //        if UserDefaults.standard.string(forKey: "username") != nil{
        //            let storyboard = UIStoryboard(name: "Main", bundle: nil)
        //            let controller = storyboard.instantiateViewController(withIdentifier: "lastViewController")
        //            self.present(controller, animated: false, completion: nil)
        //        }
        //
        self.navigationController?.isNavigationBarHidden = true
        doneButton.isEnabled = false
        userInUseLabel.isHidden = true
        // Setup the browser
        browser = NetServiceBrowser()
        browser.delegate = self
        
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
        let defaults = UserDefaults.standard
        var serverAddress = defaults.object(forKey: "serverAddress")
        while serverAddress == nil {
            userInUseLabel.text = "waiting for server response"
            sleep(1)
            serverAddress = defaults.object(forKey: "serverAddress")
        }
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
            if err != nil {
                print("error, server not responding")
            }
            else {
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
            
        }
        task.resume()
    }
    // obtain server IP address
    var browser = NetServiceBrowser()
    
    // Instance of the service that we're looking for
    var service: NetService?
    
    
    
    override func viewDidAppear(_ animated: Bool) {
        startDiscovery()
    }
    
    private func startDiscovery() {
        // Make sure to reset the last known service if we want to run this a few times
        service = nil
        
        // Start the discovery
        browser.stop()
        browser.searchForServices(ofType: "_http._tcp", inDomain: "")
    }
    
    // MARK: Service discovery
    
    func netServiceBrowserWillSearch(_ browser: NetServiceBrowser) {
        print("Search about to begin")
    }
    
    func netService(_ sender: NetService, didNotResolve errorDict: [String : NSNumber]) {
        print("Resolve error:", sender, errorDict)
    }
    
    func netServiceBrowserDidStopSearch(_ browser: NetServiceBrowser) {
        print("Search stopped")
    }
    
    func netServiceBrowser(_ browser: NetServiceBrowser, didFind svc: NetService, moreComing: Bool) {
        print("Discovered the service")
        print("- name:", svc.name)
        print("- type", svc.type)
        print("- domain:", svc.domain)
        
        // Resolve the service in 5 seconds
        service = svc
        service?.delegate = self
        
        
        
        if svc.name == "PartyTimeServer" {
            service?.resolve(withTimeout: 5)
            browser.stop()
        }
        // We dont want to discover more services, just need the first one
        if service != nil {
            return
        }
        
        // We stop after we find first service
        // browser.stop()
        
        
    }
    
    func netServiceDidResolveAddress(_ sender: NetService) {
        print("Resolved service")
        
        // Find the IPV4 address
        if let serviceIp = resolveIPv4(addresses: sender.addresses!) {
            print("Found IPV4:", serviceIp)
            let defaults = UserDefaults.standard
            defaults.set(serviceIp, forKey: "serverAddress")
            print("ho trovato il server all'indirizzo: ", serviceIp)
        } else {
            print("Did not find IPV4 address")
        }
        
        //        if let data = sender.txtRecordData() {
        //            //let dict = NetService.dictionary(fromTXTRecord: data)
        //
        //            //let value = String(data: dict["hello"]!, encoding: String.Encoding.utf8)
        //
        //            //print("Text record (hello):", value!)
        //        }
    }
    
    // Find an IPv4 address from the service address data
    func resolveIPv4(addresses: [Data]) -> String? {
        var result: String?
        
        for addr in addresses {
            let data = addr as NSData
            var storage = sockaddr_storage()
            data.getBytes(&storage, length: MemoryLayout<sockaddr_storage>.size)
            
            if Int32(storage.ss_family) == AF_INET {
                let addr4 = withUnsafePointer(to: &storage) {
                    $0.withMemoryRebound(to: sockaddr_in.self, capacity: 1) {
                        $0.pointee
                    }
                }
                
                if let ip = String(cString: inet_ntoa(addr4.sin_addr), encoding: .ascii) {
                    result = ip
                    break
                }
            }
        }
        
        return result
    }
    
}

