import Foundation
import UIKit


class DB: NSObject {
    
    var kindDict: [String:Any] = [:]
    let defaults = UserDefaults.standard
    override init() {
        
        super.init()
    }
    
    @discardableResult func storeKindsOfMusicAndCount() -> [String:Any]
    {
        
        let urlString: String = "http://192.168.2.14:5000/api/music/kindAndCount"
        guard let url = URL(string: urlString) else {
            return kindDict
        }
        let urlRequest = URLRequest(url: url)
        
        // set up the session
        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config)
        
        // make the request
        let task = session.dataTask(with: urlRequest)
        {
            (data, response, error) in
            // check for any errors
            guard error == nil else {
                return
            }
            // make sure we got data
            guard let responseData = data else {
                print("Error: did not receive data")
                return
            }
            
            // parse the result as JSON, since that's what the API provides
            do {
                guard let kinds = try JSONSerialization.jsonObject(with: responseData, options: [])
                    as? [String: Any] else {
                        print("error trying to convert data to JSON")
                        return
                }
                DispatchQueue.main.async {
                    self.kindDict = kinds
                    
                    var itemsList = [Item]()
                    for e in kinds{
                        itemsList.append(Item(kind: e.key, numberOfSongs: e.value as! Int))
                    }
                    
                }
                
                
            } catch  {
                return
            }
            
        }
        
        task.resume()
        return kindDict
        
    }
    
}


