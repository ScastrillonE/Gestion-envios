function listarClientes(){
    $('#dataTable').DataTable({
        scrollX: true,
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        fixedHeader: true,
        ajax: {
            url: window.location.pathname,
            type: "GET",
            dataType:"json",
            dataSrc:"",
        },
        columns : [
            {"data":"id"},
            {"data":"name"},
            {"data":"T_document"},
            {"data":"document"},
            {"data":"address"},
            {"data":"departamento.nombre"},
            {"data":"c_municipio.nombre"},
            {"data":"phone"},
            {"data":"cel"},
            {"data":"email"},
            {
                data: 'options',
                render: function(data,type,row){
                        var buttons = '<a href="/customer/update/' + row.id + '/"class="btn btn-warning mr-1"><i class="icon-pencil"></i></a>';
                        buttons += '<a href="/customer/delete/' + row.id + '/"class="btn btn-danger"><i class="icon-bin2"></i></a>';
                        return buttons;
                },
            }
        ],
        initComplete: function(settings,json){

        }

    });
}

function listarEnvios(){
    $('#tableShipping').DataTable({
        scrollX: true,
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: "GET",
            dataType:"json",
            dataSrc:"",
        },
        columns : [
            {"data":"id"},
            {"data":"consecutivo"},
            {"data":"cust.name"},
            {"data":"c_Tdocument"},
            {"data":"c_document"},
            {"data":"shipping_number"},
            {"data":"c_address"},
            {"data":"departamento.nombre"},
            {"data":"municip.nombre"},
            {"data":"c_phone"},
            {"data":"c_cel"},
            {"data":"s_company"},
            {
                data: 'Foto',
                render: function(data,type,row){
                    return '<img class="img-fluid img-thumbnail" src="'+row.photo+'"/>';
                },
            },

            {
                data: 'options',
                render: function(data,type,row){
                        console.log(row);
                        var buttons = '<div class=row>'+'<a href="/shipping/' + row.id + '/"class="btn btn-warning mr-1"><i class="icon-pencil"></i></a>';
                        buttons += '<a href="/shipping/delete/' + row.id + '/"class="btn btn-danger"><i class="icon-bin2"></i></a>'+ '</div>';
                        buttons += '<div class="row mt-2">'+'<a onclick="extraTable(\''+ row.status +'\' ' + ','+ '\''+ row.send_date +'\')" class="btn btn-success"><i class=" icon-eye"></i></a>';
                        buttons += '<a href="/create/pdf/' + row.id + '/"class="btn btn-primary ml-1"><i class="icon-printer"></i></a>'+'</div>';

                        return buttons;
                },

            },
        ],
        initComplete: function(settings,json){

        }

    });
}

function extraTable(status, date) {
    $('#extraTable').modal('show');
    $('#datosextra').html("<td>" +  date + "</td>" + "<td>"+status+"</td>");

}
//function addCustomer () {
//        $.confirm({
//            theme: 'modern',
//            title: 'Agregar nuevo cliente',
//            content: '' +
//            '<form action="" class="formName">' +
//            '<input type="hidden" name="csrfmiddlewaretoken" value="RdDPVYksP0vTWdoJfujBkdVWPmv0dgSflLWG5HHYzD6KjgrAA8l5b1tpjlseojaZ">' +
//            '<div class="form-group">' +
//            '<label>Ingrese nombre del cliente</label>' +
//            '<input type="text" id="id_name" name="name" class="name form-control" required />' +
//            '</div>' +
//            '<div class="form-group">' +
//            '<label>Ingrese el numero de documento</label>' +
//            '<input type="number" id="id_document" name="document" class="form-control" required />' +
//            '</div>' +
//            '<div class="form-group">' +
//            '<label>Ingrese la direccion</label>' +
//            '<input type="text" id="id_address" name="address" class="form-control" required />' +
//            '</div>' +
//            '<div class="form-group">' +
//            '<label>Ingrese el telefono</label>' +
//            '<input type="number" id="id_phone" name="phone" class="form-control"/>' +
//            '</div>' +
//            '<div class="form-group">' +
//            '<label>Ingrese el celular</label>' +
//            '<input type="number" id="id_cel" name="cel" class="form-control" required />' +
//            '</div>' +
//            '</form>',
//            buttons: {
//                formSubmit: {
//                    text: 'Guardar',
//                    btnClass: 'btn-blue',
//                    action: function () {
//
//                       var data = $(".formName").serialize();
//
//                       $.ajax({
//                            url: 'customer/create',
//                            type: 'POST',
//                            data:data,
//                            dataType: 'json',
//                       }).done(function(data){
//                            listarClientes();
//
//                       }).fail(function (data) {
//                            $.alert({
//                                title: 'Ocurrio un error',
//                                content: 'Esto puede ser por que el usuario ya se encuentra registrado',
//                            });
//                       });
//                    }
//                },
//                cancel: {
//                    text: 'Cancelar',
//                    btnClass: 'btn-danger',
//                },
//            },
//
//
//    });
//
//}

function takePhoto(){
  var player = document.getElementById('player');
  var snapshotCanvas = document.getElementById('snapshot');
  var captureButton = document.getElementById('capture');
  var img = document.getElementById('img');
  var im64 = document.getElementById('id_photo');
  var previewimg = document.getElementById('preview');

  var handleSuccess = function(stream) {
    // Attach the video stream to the video element and autoplay.
    player.srcObject = stream;
  };

  captureButton.addEventListener('click', function() {
    var context = snapshot.getContext('2d');
    // Draw the video frame to the canvas.
    context.drawImage(player, 0, 0, snapshotCanvas.width,
        snapshotCanvas.height);
    im64.value= snapshot.toDataURL('image/png');
    previewimg.src = snapshot.toDataURL('image/png');
  });


  navigator.mediaDevices.getUserMedia({video: true})
      .then(handleSuccess);
}

function autocomplete_customer(){
    $("#id_customer").on("change",function(){
        var id = $("#id_customer").val()
        $.ajax({
            url: window.location.pathname,
            type: "POST",
            dataType:"json",
            data: {
                'action': 'search_data_customer',
                'id': id,
            }
        }).done(function(data){
//            var Tdocument = data[0]['T_document'];
//            var document = data[0]['document'];
//            var address = data[0]['address'];
//            var phone = data[0]['phone'];
//            var cel = data[0]['cel'];
            var items = data[0];
            $("#id_c_Tdocument").val(data[0]['T_document']);
            $("#id_c_document").val(data[0]['document']);
            $("#id_c_address").val(data[0]['address']);
            $("#id_c_phone").val(data[0]['phone']);
            $("#id_c_cel").val(data[0]['cel']);
            $("#id_c_email").val(data[0]['email']);
            $('#id_c_department').val(items.departamento.id).trigger('change');
            $("#id_c_municipio").val(items.municipio).trigger('change');

//            console.log(items.municipio);
        });
    });
}


$(document).ready(function(){
    listarClientes();
    listarEnvios();

});