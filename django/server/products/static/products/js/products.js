const renderProduct = ({id, name, description, cost, image}) => (
    `
        <div class="mac">
        <div class="products_itemer">
            <a href="/products/${ id }" class="products_item-link">
            <img src="${ image }" alt="${ name }" class="products__item-image" width="250px" height="250px">
            <h2 class="products_item-name">
               ${ name }
            </h2>
            </a>
            ${ cost }
            <h4 class="products_item-cost">
                Price : ${ cost } $ 
            </h4> 
            <a href=""></a>
        </div>
        </div>
    
    `
)