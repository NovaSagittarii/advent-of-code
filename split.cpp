std::string s = "scott>=tiger>=mushroom";
std::string delimiter = ">=";

std::vector<std::string> split(std::string s, std::string delimiter){
    std::vector<std::string> results;
    size_t pos = 0;
    std::string token;
    while ((pos = s.find(delimiter)) != std::string::npos) {
        token = s.substr(0, pos);
        results.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    return results;
}