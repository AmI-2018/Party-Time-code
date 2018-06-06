
import Foundation
import UIKit

class Beacon: NSObject {
    
    var room: String
    var uuid: String
    var minor: Int
    var major: Int
   
    
    init(room:String, uuid: String, minor: Int?=nil, major: Int?=nil) {
        self.room = room
        self.uuid = uuid
        self.minor = minor!
        self.major = major!
        
        super.init()
    }
    
    func toPrint() -> String {
        return "room:\(self.room), uuid:\(self.uuid), major:\(self.major), minor:\(self.minor)"
    }
        
//    func firstChoise(choise: String) {
//        self.preference = 1
//        self.alreadyAdded = true
//    }
    
    
    
    
}
