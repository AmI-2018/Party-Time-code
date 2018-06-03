import Foundation
import UIKit


class DB: NSObject {
    
    func getKindsOfMusicAndCount() -> [String:Any]
    {
        
        var ret = [String:Any]()
        
        let urlString: String = "http://192.168.2.14:5000/api/music/kindAndCount"
        guard let url = URL(string: urlString) else { return ret}
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
                print("error calling GET on /todos/1")
                print(error!)
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
                            // now we have the todo
                            // let's just print it to prove we can access it
                            print("The todo is: " + kinds.description)
                            print(kinds.keys)
                            ret = kinds
                            
                        } catch  {
                            print("error trying to convert data to JSON")
                            return
                        }
            
            
            
       
        }
        task.resume()
        return ret
        
    }
    
    
    
}


