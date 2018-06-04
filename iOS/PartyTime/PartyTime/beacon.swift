
import Foundation
import UIKit

class Beacon: NSObject {
    
    var room: String
    var uuid: String
    var minor: Int
    var major: Int
   
    
    init(room:String, uuid: String, minor: Int, major: Int) {
        self.room = room
        self.uuid = uuid
        self.minor = minor
        self.major = major
        
        super.init()
    }
    
//    func firstChoise(choise: String) {
//        self.preference = 1
//        self.alreadyAdded = true
//    }
    
    
    
    
}
