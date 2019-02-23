class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None): #, total=0 , items=[]):
        self.employee_discount = employee_discount
        self.total=0
        self.items=[]
        
    def add_item(self, name, price, quantity=1):
        q=0 
        while q <quantity :
            self.items.append({name : price})
            self.total+= price
            q+=1
        return self.total
    
    
    def get_list_of_prices(self):
        list_items=self.items
        
        list_list_prices = []
        for item in list_items:
            list_list_prices.append(list(item.values()))
            
        list_prices=[val for sublist in list_list_prices for val in sublist]
        return list_prices          
    

    def mean_item_price(self):
        price_list=self.get_list_of_prices()
        return sum(price_list)/len(price_list)
    
    

    def median_item_price(self):
        
        s =sorted(self.get_list_of_prices()) 
    
        # Check for even/odd and perform calculations accordingly - use if-else 
        if len(s) % 2 == 0 :
            mid_idx=int((len(s)/2)-1)
            med=(sum(s[mid_idx:mid_idx+2]))/2
        else:
            mid_idx=int(len(s)//2)
            med= s[mid_idx]

        return med
    


    def apply_discount(self):
        if self.employee_discount:
            new_total=self.total*((100-self.employee_discount)/100)
            return new_total
        else:
            return print('Sorry, there is no discount to apply to your cart :("')
       

    def void_last_item(self):
        if len(self.items)==0:
            return print('There are no items in your cart!')
        else:
            last_item=self.items[-1]
            for k,v in last_item.items():
                print(k,v)
                self.total-=last_item[k] #.values(0)
        self.items.pop()
        
        