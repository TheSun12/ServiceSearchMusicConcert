function buy_ticket(concId){
    alert(concId)
    var value = concId
    $.ajax({
        url: '/buy_with_card',
        type: 'POST',
        data: {'data': value}
    })
}