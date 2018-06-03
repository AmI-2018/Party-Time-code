import Foundation
import UIKit

class Item: NSObject {
    
    var kind: String
    var numberOfSongs: Int
    var alreadyAdded: Bool
    
    init(kind: String, numberOfSongs: Int) {
        self.kind = kind
        self.numberOfSongs = numberOfSongs
        self.alreadyAdded = false
        
        super.init()
    }
    
    
}
