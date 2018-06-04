import Foundation
import UIKit

class Item: NSObject {
    
    var kind: String
    var numberOfSongs: Int
    var alreadyAdded: Bool
    // 1 -> high, 3-> low
    var preference: Int
    
    
    init(kind: String, numberOfSongs: Int) {
        self.kind = kind
        self.numberOfSongs = numberOfSongs
        self.alreadyAdded = false
        self.preference = -1
        
        super.init()
    }
    
    func firstChoise(choise: String) {
        self.preference = 1
        self.alreadyAdded = true
    }
    
    func secondChoise(choise: String) {
        self.preference = 1
        self.alreadyAdded = true
        
    }
    
    func thirdChoise(choise: String) {
        self.preference = 1
        self.alreadyAdded = true
        
    }
    
    
    
}
