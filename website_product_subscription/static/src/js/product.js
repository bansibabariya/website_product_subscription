odoo.define('website_product_subscription.product', function (require) {

	'use strict';
	var ajax= require('web.ajax')
	var rpc= require('web.rpc')
	$(document).ready(function(){

        var has_submit_address_clicked = false;
        $("#product_subscribe_form").on('submit' ,function(e) {
        e.preventDefault();
        if (!has_submit_address_clicked){
            var email = $('#product_subscribe_email').val();
            var product_id = $('#product_subscribe_id').val();
            if(email && product_id){
                rpc.query({route: '/product_subscription_form_submit',
                    params:{
                        email:email,
                        product_id:product_id,
                    },
                }).then(function(result) {
                    if(result){
                        $('#subscribe_div').addClass('d-none')
                        $('#product_status').removeClass('d-none')
                    }
                });
            }
        }
	});
	});


})