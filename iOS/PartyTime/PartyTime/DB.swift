import Foundation
import UIKit


class DB: NSObject {
    
    var kindDict: [String:Any] = [:]
    let defaults = UserDefaults.standard
    override init() {
        
        super.init()
        //        self.kindDict = getKindsOfMusicAndCount()
        //        print("Dentro il DB.sw")
        //        print(kindDict.count)
        //        self.kindDict = getKindsOfMusicAndCount()
        
    }
    
    @discardableResult func storeKindsOfMusicAndCount() -> [String:Any]
    {
        
        //        var ret = [String:Any]()
        
        let urlString: String = "http://192.168.2.14:5000/api/music/kindAndCount"
        guard let url = URL(string: urlString) else {
            print("error in url")
            return kindDict
            
            
        }
        let urlRequest = URLRequest(url: url)
        
        
        // set up the session
        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config)
        
        var responseDict = [String:Any]()
        
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
                //                            print("The todo is: " + kinds.description)
                //                            print(kinds.keys)
                //                            print("la variabile senza nulla: \(kinds)")
                //                            ret = kinds
                
                DispatchQueue.main.async {
                    self.kindDict = kinds
                    responseDict = kinds
//                    completionHandler(kinds)
                    print("kindDict inside function \(self.kindDict)")
                    print("kinds inside function \(kinds)")
                    var itemsList = [Item]()
                    for e in kinds{
                        itemsList.append(Item(kind: e.key, numberOfSongs: e.value as! Int))
                    }
//                    self.defaults.set(itemsList, forKey: "kinds")
                    for i in itemsList{
                        print("itemsList \(i.kind) \(i.numberOfSongs) \(i.alreadyAdded)")
                    }
                    
                }
                
                
            } catch  {
                print("error trying to convert data to JSON")
                return
            }
            
        }
        
        task.resume()
//        
//        print("kindDict inside DB")
//        print(kindDict)
//        print("responseDict inside DB")
//        print(responseDict)
//        
        
        return kindDict
        
    }
    
//
//    enum Result<Value> {
//        case success(Value)
//        case failure(Error)
//    }
//
    
//    func getKindsOfMusicAndCount(for userId: Int, completion: () {
//        var urlComponents = URLComponents()
//        urlComponents.scheme = "http"
//        urlComponents.host = "192.168.2.14:5000"
//        urlComponents.path = "/api/music/kindAndCount"
////        let userIdItem = URLQueryItem(name: "userId", value: "\(userId)")
////        urlComponents.queryItems = [userIdItem]
//        guard let url = urlComponents.url else { fatalError("Could not create URL from components") }
//
//        var request = URLRequest(url: url)
//        request.httpMethod = "GET"
//
//        let config = URLSessionConfiguration.default
//        let session = URLSession(configuration: config)
//
//        let task = session.dataTask(with: request) { (responseData, response, responseError) in
//            DispatchQueue.main.async {
//                if let error = responseError {
//                    completion?(.failure(error))
//                } else if let jsonData = responseData {
//                    // Now we have jsonData, Data representation of the JSON returned to us
//                    // from our URLRequest...
//
//                    // Create an instance of JSONDecoder to decode the JSON data to our
//                    // Codable struct
//                    let decoder = JSONDecoder()
//
//                    do {
//                        // We would use Post.self for JSON representing a single Post
//                        // object, and [Post].self for JSON representing an array of
//                        // Post objects
//                        let posts = try decoder.decode([Post].self, from: jsonData)
//                        completion?(.success(posts))
//                    } catch {
//                        completion?(.failure(error))
//                    }
//                } else {
//                    let error = NSError(domain: "", code: 0, userInfo: [NSLocalizedDescriptionKey : "Data was not retrieved from request"]) as Error
//                    completion?(.failure(error))
//                }
//            }
//        }
//
//        task.resume()
//    }
//
    
    
    
}


