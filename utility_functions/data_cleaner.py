class data_cleaner:
    def __init__(self, child_element):
        self.child_element = child_element

    def clean(self):
        print('Data has been fetched, and is at cleaning Stage!!!!')
        sett = {''}
        for i in self.child_element:
            child = i.get_attribute('href')
            if child is not None and 'deta' in child:
                print(child)
                sett.add(child)
        data = list(sett)
        data.pop(0)
        return data
