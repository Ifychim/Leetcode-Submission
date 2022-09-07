/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
        let anaMap = {};
    for(let string of strs){
        let temp = string.split('').sort()
        anaMap[temp] ? anaMap[temp].push(string) : anaMap[temp] = [string]
    }
   
    //let result = Array.from(Object.values(anaMap))
    return Array.from(Object.values(anaMap));

};