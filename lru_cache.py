def lru_cache(max_size):
    hashmap = {}
    queue = []

    def lru_cache_wrapper(func):
        def lru_cache_get(*key):
            if key in hashmap:
                queue.pop(queue.index(key))
                return hashmap[key]
            value = func(*key)

            hashmap[key] = value
            queue.insert(0, key)

            if(len(queue) > max_size):
                hashmap.pop(queue[max_size])
                queue.pop(max_size)

            return value
        return lru_cache_get
    return lru_cache_wrapper
