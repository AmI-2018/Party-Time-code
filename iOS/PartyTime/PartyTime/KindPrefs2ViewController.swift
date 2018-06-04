//
//  KindPrefs2ViewController.swift
//  PartyTime
//
//  Created by jazz on 3/6/18.
//  Copyright © 2018 alessio-zamparelli. All rights reserved.
//

import UIKit

class KindPrefs2ViewController: UIViewController, UITableViewDataSource, UITableViewDelegate {

    @IBOutlet weak var tableOutlet: UITableView!
    @IBOutlet weak var doneButton: UIButton!
    
    var itemsList = [Item]()
    var selectedList = [Item]()
    var selectedCell = UITableViewCell()
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
        doneButton.isEnabled = false
        doneButton.alpha = 0.6
        
//
//        for i in itemsList{
//            print("\(i.kind) \(i.numberOfSongs) \(i.alreadyAdded) \(i.preference)")
//        }
//        for i in selectedList{
//            print("\(i.kind) \(i.numberOfSongs) \(i.alreadyAdded) \(i.preference)")
//        }
        
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
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {

        return itemsList.count
        
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        // Create an object of the dynamic cell “PlainCell”
        let cell = tableView.dequeueReusableCell(withIdentifier: "PlainCell2", for: indexPath)
        // Depending on the section, fill the textLabel with the relevant text
        
        
        let cellElementKind = itemsList[indexPath.row].kind
        let cellElementSongs = itemsList[indexPath.row].numberOfSongs
        cell.textLabel?.text = cellElementKind
        cell.detailTextLabel?.text = String(cellElementSongs)
    
        return cell
        
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.destination is KindPrefs3ViewController
        {
            
            let selectedKind = selectedCell.textLabel!.text!
            for i in itemsList{
                if i.kind == selectedKind{
                    
                    i.firstChoise(choise: selectedKind)
                    selectedList.append(i)
                    itemsList.remove(at: itemsList.index(of: i)!)
                    
                }
                
                print("ItemsList è lunga: \(itemsList.count)")
                print("Alla seconda scelta risulta: \(i.kind) \(i.preference)")
                
            }
            
            let vc = segue.destination as? KindPrefs3ViewController
            vc?.itemsList = self.itemsList
            vc?.selectedList = self.selectedList
//
//            let vc = segue.destination as? KindPrefs3ViewController
//            vc?.itemsList = self.itemsList
//            vc?.selectedList = self.selectedList
//
//            let indexPath = tableOutlet.indexPathForSelectedRow //optional, to get from any UIButton for example
//
//            let currentCell = tableOutlet.cellForRow(at: indexPath!)
//            let selectedKind = currentCell!.textLabel!.text!
//            print("Cella selezionata: \(selectedKind)")
//
//            var index = 0
//            for i in itemsList{
//                if i.kind == selectedKind{
//                    i.firstChoise(choise: selectedKind)
//                    selectedList.append(i)
//                    itemsList.remove(at: index)
//                    break
//                }
//                index += 1
//                print("Alla seconda scelta risulta: \(i.kind) \(i.preference)")
//            }
        }
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

















