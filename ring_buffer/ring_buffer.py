class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    length = len([x for x in self.storage if x is not None])
    if length < self.capacity:
      self.storage.pop(0)
      self.storage.append(item)
    else: 
      self.storage[self.current] = item
      self.current = (self.current + 1) % length
    

  def get(self):
    return [x for x in self.storage if x is not None]
