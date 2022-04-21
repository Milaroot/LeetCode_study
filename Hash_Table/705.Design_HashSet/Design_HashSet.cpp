class MyHashSet {
public:
    int *mp = new int[1000001]{0};
    MyHashSet() {

    }
    
    void add(int key) {
        mp[key] = 1;
    }
    
    void remove(int key) {
        mp[key] = 0;
    }
    
    bool contains(int key) {
        return mp[key];
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */