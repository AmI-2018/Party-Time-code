//
//  KindPrefs1ViewController.swift
//  PartyTime
//
//  Created by jazz on 3/6/18.
//  Copyright © 2018 alessio-zamparelli. All rights reserved.
//

import UIKit

class KindPrefs1ViewController: UIViewController, UITableViewDataSource {

//    var testValues = ["Ciccio1":10, "Ciccio2":20, "Ciccio3":30]
    
//    var testValuesKeys = ["Ciccio1", "Ciccio2", "Ciccio3"]
    
    var kindsDict = [String:Any]()
    
//    var db = DB()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        navigationItem.hidesBackButton = true
        
        // ottengo i val
        let db = DB()
//        kindsDict = db.getKindsOfMusicAndCount()
        kindsDict = db.getKindsOfMusicAndCount()
        print("Sto stampando: kindsDict")
        print(kindsDict)
//        var db = DB()
//        var res = db.getKindsOfMusicAndCount()
//        let keys = Array(res.keys)
//        print("Stampo le keys \(keys)")
//        print("Stampo i values \(testValues.values)")
//        print("Count: \(kindsDict.count)")
        
//        print("String(Array(kindsDict.keys)[indexPath.row])")
//        print(String(Array(kindsDict.keys)[0]))
//        print(db.getKindsOfMusicAndCount())
        
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
//    let sections = ["Fruit", "Vegetables"]
    

//    func tableView(_ tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
//        // here the title for the section
//        return "tette"
//    }
//
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return kindsDict.count
        
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        // Create an object of the dynamic cell “PlainCell”
        let cell = tableView.dequeueReusableCell(withIdentifier: "PlainCell", for: indexPath)
        // Depending on the section, fill the textLabel with the relevant text
        
        cell.textLabel?.text = String(Array(kindsDict.keys)[indexPath.row])
//        cell.textLabel?.text = testValuesKeys[indexPath.row]
        
        return cell
        }
    
    
//
//    var itemStore = ItemStore()
//
//    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
//        // // Create an instance of UITableViewCell with default apparence
//        // let cell = UITableViewCell(style: .value1, reuseIdentifier: "UITableViewCell")
//
//        // Get a new or recycled cell
//        let cell = tableView.dequeueReusableCell(withIdentifier: "UITableViewCell", for: indexPath)
//
//        // Set the text on the cell with the description of the item
//        // that is at the nth index of the items, where n = row this cell
//        // will appear in on the tableView
//
//        let item = itemStore.allItems[indexPath.row]
//
//        cell.textLabel?.text = item.kind
//        cell.detailTextLabel?.text = String(item.numberOfSongs)
//
//        return cell
//    }
//
//    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
//        return itemStore.allItems.count
//    }
//

}
