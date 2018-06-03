import Foundation
import UIKit

class ItemStore {
    
    var allItems = [Item]()
    
    func createItem() {
        let db = DB()
        
        let res = db.getKindsOfMusicAndCount()
        for i in res{
            let newItem = Item(kind: i.key, numberOfSongs: i.value as! Int)
            allItems.append(newItem)
            print("kind \(newItem.kind)")
            print("number of songs \(String(newItem.numberOfSongs))")
        }
        
    }
    
    init() {
        createItem()
    }
    
    
    
    
    
    
    
    
    
}


