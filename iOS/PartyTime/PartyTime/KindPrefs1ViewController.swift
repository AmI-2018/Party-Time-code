//
//  KindPrefs1ViewController.swift
//  PartyTime
//
//  Created by jazz on 3/6/18.
//  Copyright © 2018 alessio-zamparelli. All rights reserved.
//

import UIKit

class KindPrefs1ViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {
    
    @IBOutlet weak var tableOutlet: UITableView!
    @IBOutlet weak var doneButton: UIButton!
    
    var itemsList = [Item]()
    var selectedList = [Item]()
    var selectedCell = UITableViewCell()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        navigationItem.hidesBackButton = true
        doneButton.isEnabled = false
        doneButton.alpha = 0.6
        parseJSON()
        
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
        
        return itemsList.count
        
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        // Create an object of the dynamic cell “PlainCell”
        let cell = tableView.dequeueReusableCell(withIdentifier: "PlainCell1", for: indexPath)
        
        // Depending on the section, fill the textLabel with the relevant text
        let cellElementKind = itemsList[indexPath.row].kind
        let cellElementSongs = itemsList[indexPath.row].numberOfSongs
        cell.textLabel?.text = cellElementKind
        cell.detailTextLabel?.text = String(cellElementSongs)
        
        return cell
        
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.destination is KindPrefs2ViewController
        {
            
            //            let indexPath = tableOutlet.indexPathForSelectedRow //optional, to get from any UIButton for example
            //
            //            let currentCell = tableOutlet.cellForRow(at: indexPath!)
            //            let selectedKind = currentCell!.textLabel!.text!
            //
            //            print("Cella selezionata: \(selectedKind)")
            //
            //            for i in itemsList{
            //                if i.kind == selectedKind{
            //
            //                    i.firstChoise(choise: selectedKind)
            //                    selectedList.append(i)
            //                    itemsList.remove(at: itemsList.index(of: i)!)
            //
            //                }
            //
            //                print("ItemsList è lunga: \(itemsList.count)")
            //                print("Alla prima scelta risulta: \(i.kind) \(i.preference)")
            //
            //            }
            //
            
            let selectedKind = selectedCell.textLabel!.text!
            for i in itemsList{
                if i.kind == selectedKind{
                    
                    i.firstChoise(choise: selectedKind)
                    selectedList.append(i)
                    itemsList.remove(at: itemsList.index(of: i)!)
                    
                }
                
                print("ItemsList è lunga: \(itemsList.count)")
                print("Alla prima scelta risulta: \(i.kind) \(i.preference)")
                
            }
            
            let vc = segue.destination as? KindPrefs2ViewController
            vc?.itemsList = self.itemsList
            vc?.selectedList = self.selectedList
            
            let defaults = UserDefaults.standard
            print("Setting the pref1 (\(selectedKind)) inside defaults")
            defaults.set(selectedKind, forKey: "pref1")
            
            
            
        }
    }
    
    
    
    func parseJSON() {
        print("entrato nel parser")
        let url = URL(string: "http://192.168.2.14:5000/api/music/kindAndCount")
        let task = URLSession.shared.dataTask(with: url!) {(data, response, error) in
            
            guard error == nil else { fatalError("returning error") }
            
            guard let content = data else { fatalError("not returning data") }
            
            guard let json = (try? JSONSerialization.jsonObject(with: content, options: JSONSerialization.ReadingOptions.mutableContainers)) as? [String: Any] else { fatalError("Not containing JSON") }
            
            for e in json{
                self.itemsList.append(Item(kind: e.key, numberOfSongs: (e.value as! Int)))
            }
            
            DispatchQueue.main.async {
                self.tableOutlet.reloadData()
            }
            
        }
        
        task.resume()
        
    }
    
    
    
    override func viewWillAppear(_ animated: Bool) {
        if let index = self.tableOutlet.indexPathForSelectedRow{
            self.tableOutlet.deselectRow(at: index, animated: true)
        }
        
    }
    
    
    
    func tableView(_ tableView: UITableView, didSelectRowAt selectedIndex: IndexPath) {
        
        //        tableView.deselectRow(at: indexPath, animated: true)
        
        doneButton.alpha = 1
        doneButton.isEnabled = true
        
        //        let indexPath = tableOutlet.indexPathForSelectedRow //optional, to get from any UIButton for example
        //        self.tableOutlet.deselectRow(at: selectedIndex, animated: true)
        
        //        let currentCell = tableOutlet.cellForRow(at: selectedIndex)
        selectedCell = tableView.cellForRow(at: selectedIndex)!
        //        let selectedKind = currentCell!.textLabel!.text!
        let selectedKind = selectedCell.textLabel!.text! // da togliere!
        
        print("Cella selezionata: \(selectedKind)")
        
    }
    
    
    
    
}

