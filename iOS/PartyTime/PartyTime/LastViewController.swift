//
//  LastViewController.swift
//  PartyTime
//
//  Created by jazz on 4/6/18.
//  Copyright © 2018 alessio-zamparelli. All rights reserved.
//

import UIKit

class LastViewController: UIViewController {

    var selectedList = [Item]()

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

    func createUser() {
        print("entrato nel createUser")
        let url = URL(string: "http://192.168.2.14:5000/api/music/kindAndCount")
        let task = URLSession.shared.dataTask(with: url!) {(data, response, error) in
            
            guard error == nil else { fatalError("returning error") }
            
            guard let content = data else { fatalError("not returning data") }
            
            guard let json = (try? JSONSerialization.jsonObject(with: content, options: JSONSerialization.ReadingOptions.mutableContainers)) as? [String: Any] else { fatalError("Not containing JSON") }
//            
//            for e in json{
//                self.itemsList.append(Item(kind: e.key, numberOfSongs: (e.value as! Int)))
//            }
//            
//            DispatchQueue.main.async {
//                self.tableOutlet.reloadData()
//            }
//            
        }
        
        task.resume()
    }
}
