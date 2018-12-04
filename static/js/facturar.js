var lineasDeFactura = [];
var total = 0.0;
var totalHTML = document.getElementById('total');
var articulosHTML = document.getElementById('articulos');
var total = 0.0;
var articulos = 0.0;


var producto
function obtenerProducto(){

    var tbodyLinea = document.getElementById('linea');
    var fila = tbodyLinea.insertRow();

    var columnaCodigo = fila.insertCell();
    var columnaProducto = fila.insertCell();
    var columnaMarca = fila.insertCell();
    var columnaDescripcion = fila.insertCell();
    var columnaPrecio = fila.insertCell();
    var columnaCantidad = fila.insertCell();
    var columnaSubtotal = fila.insertCell();
    var columnaIcono = fila.insertCell();



    var cantidad = document.getElementById('cantidad').value;
    var cantida = document.createTextNode(cantidad);
    columnaCantidad.appendChild(cantida);

    var codigo = document.getElementById('codigo').value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

           producto = JSON.parse(xhttp.responseText);
           //console.log(xhttp.responseText);
           //console.log(producto);
           //console.log(producto.length);
           //console.log(producto[0].fields.nombre);
            var codig = document.createTextNode(producto[0].fields.codigo);
            columnaCodigo.appendChild(codig);

            var product = document.createTextNode(producto[0].fields.nombre);
            columnaProducto.appendChild(product);

             var marc = document.createTextNode(producto[0].fields.marca);
             columnaMarca.appendChild(marc);

             var descripcio = document.createTextNode(producto[0].fields.descripcion);
             columnaDescripcion.appendChild(descripcio);

             var preci = document.createTextNode('$' + producto[0].fields.precio);
             columnaPrecio.appendChild(preci);

             var sub = Number.parseFloat(producto[0].fields.precio * cantidad * 1.00).toFixed(2)
             var subtota = document.createTextNode('$' + sub);
             columnaSubtotal.appendChild(subtota);


             var i = document.createElement("i");
             i.setAttribute('class','fa fa-trash');
             i.setAttribute('aria-hidden','true');
             var boton = document.createElement('button');
             boton.setAttribute('type','button');
             boton.setAttribute('class','btn btn-light');
             boton.setAttribute('style','padding-left: 0rem;padding-right: 0rem;padding-top: 0.0rem;padding-bottom: 0rem;border-left-width: 0px;border-top-width: 0px;border-right-width: 0px;border-bottom-width: 0px;');
             //Poner evento al boton
             boton.setAttribute('onclick','eliminar()');
             boton.appendChild(i);

             columnaIcono.appendChild(boton);

             agregarLinea();

       }
    };
    xhttp.open("GET", "/venta/producto/"+codigo+"/", true);
    xhttp.send();
}

function agregarLinea(){
    var cant = document.getElementById('cantidad').value;

    var linea = {
        codigo: producto[0].fields.codigo,
        producto: producto[0].fields.nombre,
        marca: producto[0].fields.marca,
        descripcion: producto[0].fields.descripcion,
        precio: producto[0].fields.precio * 1.00,
        cantidad: cant,
        subtotal: producto[0].fields.precio * cant * 1.00
    };
    //console.log(linea);

    lineasDeFactura.push(linea);
    total += linea.subtotal;

    console.log(lineasDeFactura);
    //console.log('Total: ' + total);
    articulos += cant * 1;
    //console.log('Total articulos: ' + articulos);

    totalHTML.textContent = '$' + Number.parseFloat(total).toFixed(2);
    articulosHTML.textContent = articulos;

}

function eliminar(){

}

function finalizar() {

    //Conseguimos el id del cliente seleecionado
    var listaClientes = document.getElementById('clientes');
    var idCliente = listaClientes.options[listaClientes.selectedIndex].value;
    var clienteSeleccionado = listaClientes.options[listaClientes.selectedIndex]
    console.log(idCliente);

    if(listaClientes.selectedIndex == 0 || lineasDeFactura.length == 0 ){
        return;
    }else{
        var datos = JSON.stringify(lineasDeFactura);
        var params = "registros=" + encodeURI(datos) + "&idCliente=" + idCliente + '&total=' + total;
        var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        var xhttp = new XMLHttpRequest();

        xhttp.open("POST", "/venta/guardar", true);
        xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhttp.setRequestHeader('X-CSRFToken', csrfToken);
        xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200){
            // esto inprime la respuesta
            console.log(xhttp.responseTex);
            window.location.href="/venta/facturar";
            }
        }
        xhttp.send(params);
        console.log(params);
    }

}


