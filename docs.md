# Purchase order example 

PO number: 1
Company id: 2
Company name: Pikachu Labs 
Product/Service description: 1 year of paper
PO amount: $1000
Start time: 01.01.2022
End time: 12.31.2022


PO number: 2
Company id: 2
Company name: Pikachu Labs 
Product/Service description: gummibears for half a year (team bulding)
PO amount: $4000
Start time: 01.01.2022
End time: 06.30.2022

# Invoices raised against the purchase order

Vendor company id: 1
Company name: Pikachu Labs 
Invoice number: AB-1234
Invoiced amount: $50
Invoice date: 01.15.2022
possibly: attachment of invoice pdf (we'll ignore this)




# Abandoned code on invoice details (out of scope)

```js 
         
<section class="js-items-container"></section>
<button class="js-new-item">Add item</button> 

    <script>
let item_num = 1;
let template = (event) => {  
    event.preventDefault();
    document.querySelector('.js-items-container').innerHTML += `
    <div class="item-row">
        <label>
            Item name:
            <input type="text" name="item-name-1" />
        </label>
        <label>
            Quantity:
            <input type="text" name="item-quantity-1" />
        </label>        
        <label>
            Cost per item:
            <input type="text" name="item-cost-1" />
        </label> 
    </div>    
    `;
}
document
    .querySelector('.js-new-item')
    .addEventListener('click', template);

    </script>  
```