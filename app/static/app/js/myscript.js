$('#slider1, #slider2, #slider3').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})

$('.plus-cart').click(function(){
    console.log("Plus Clicked")
    var eml = this.parentNode.children[2]
    var id = $(this).attr('pid').toString();
    // console.log(id);
    $.ajax({
        type:"GET",
        url:"/plus_cart",
        data:{
           prod_id:id
        },
        success : function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            
            console.log(data)
            console.log("success")
        }
    })
})
$('.minus-cart').click(function(){
    console.log("Plus Clicked")
    var eml = this.parentNode.children[2]
    var id = $(this).attr('pid').toString();
    // console.log(id);
    $.ajax({
        type:"GET",
        url:"/minus_cart",
        data:{
           prod_id:id
        },
        success : function(data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount

            console.log(data)
            console.log("success")
        }
    })
})


$('.remove-cart').click(function(){
    console.log("Plus Clicked")
    var eml = this
    var id = $(this).attr('pid').toString();
    // console.log(id);
    $.ajax({
        type:"GET",
        url:"/remove_cart",
        data:{
           prod_id:id
        },
        success : function(data){
            console.log("Delete")

            //eml.innerText = data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
            console.log(data)
            console.log("success")
        }
    })
})