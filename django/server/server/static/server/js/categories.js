const renderCategory = ({id, name}) => (
    `
        <li class="mac">
        <div class="products_itemer">

            <a href="/categories/${ id }" class="products_item-link">
            <img src="/../static/products/img/fon.jpg" alt="none" class="imagegege" width="250px" height="250px">
            <h2 class="products_item-name">
                ${ name }
            </h2>
            </a>
            <a href=""></a>

        </div>
        </li>
    
    `
)