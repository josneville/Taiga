var request = require('superagent')
var nodemailer = require('nodemailer');

module.exports = {
	send: function(req, res) {
		var randAcct = Math.floor(Math.random() * (104999 - 100000) + 100000)
		var headers = {'username': 'giveitatry', 'password': 'Sh0wT!me', 'Content-Type': 'application/json'}
		request
		   .post('https://syf2020.syfwebservices.com/syf/nextMostLikelyPurchase')
		   .send({ 'accountNum': String(randAcct)})
		   .set(headers)
		   .end(function(err, response){
		     if (err || !response.ok) {
		     	console.log(response)
		     	return res.status(400).send({message: err})
		     } else {
		     	var body = response.body
		     	var cats = body['categories']
		     	var max = {'categoryName': 'default', 'probability': 0}
		     	for (var i = 0; i < cats.length; i++) {
		     		if (max['probability'] < cats[i]['probability']) {
		     			max = cats[i]
		     		}
		     	}

		     	var html="";
				html += "<!DOCTYPE html PUBLIC \"-\/\/W3C\/\/DTD XHTML 1.0 Transitional\/\/EN\" \"http:\/\/www.w3.org\/TR\/xhtml1\/DTD\/xhtml1-transitional.dtd\">";
				html += "<html>";
				html += "<head>";
				html += "<title>Responsive Email Template<\/title>";
				html += "<meta http-equiv=\"Content-Type\" content=\"text\/html\" charset=\"UTF-8\" \/>";
				html += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" \/>";
				html += "<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\" \/>";
				html += "<style type=\"text\/css\">";
				html += "\/* Stop WebKit from changing text sizes *\/";
				html += "body, table, td, a {";
				html += "	-webkit-text-size-adjust: 100%;";
				html += "	-ms-text-size-adjust: 100%;";
				html += "}";
				html += "body {";
				html += "	height: 100% !important;";
				html += "	margin: 0 !important;";
				html += "	padding: 0 !important;";
				html += "	width: 100% !important;";
				html += "}";
				html += "\/* Removes spacing between tables in Outlook 2007+ *\/";
				html += "table, td {";
				html += "	mso-table-lspace: 0pt;";
				html += "	mso-table-rspace: 0pt;";
				html += "} ";
				html += "img {";
				html += "	border: 0;";
				html += "	line-height: 100%;";
				html += "	text-decoration: none;";
				html += "	-ms-interpolation-mode: bicubic; \/* Smoother rendering in IE *\/";
				html += "}";
				html += "table {";
				html += "	border-collapse: collapse !important;";
				html += "}";
				html += "\/* iOS Blue Links *\/";
				html += "a[x-apple-data-detectors] {";
				html += "	color: inherit !important;";
				html += "	text-decoration: none !important;";
				html += "	font-size: inherit !important;";
				html += "	font-family: inherit !important;";
				html += "	font-weight: inherit !important;";
				html += "	line-height: inherit !important;";
				html += "}";
				html += "\/* Table fix for Outlook *\/";
				html += "table {";
				html += "	border-collapse:separate;";
				html += "}";
				html += ".ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td {";
				html += "	line-height: 100%;";
				html += "}";
				html += ".ExternalClass {";
				html += "	width: 100%;";
				html += "}";
				html += "\/* Mobile Styling *\/";
				html += "@media screen and (max-width: 525px){";
				html += ".wrapper {";
				html += "	width: 100% !important;";
				html += "	max-width: 100% !important;";
				html += "}";
				html += ".hide-element {";
				html += "	display: none !important;";
				html += "}";
				html += ".img-max {";
				html += "	max-width: 100% !important;";
				html += "	width: 100% !important;";
				html += "	height: auto !important;";
				html += "}";
				html += ".table-max {";
				html += "	width: 100% !important;";
				html += "}";
				html += ".mobile-btn-container {";
				html += "	margin: 0 auto;";
				html += "	width: 90% !important;";
				html += "}";
				html += ".mobile-btn {";
				html += "	padding: 15px !important;";
				html += "	border: 0 !important;";
				html += "	font-size: 16px !important;";
				html += "	display: block !important;";
				html += "}";
				html += ".text-center {";
				html += "	text-align:center !important;";
				html += "}";
				html += "}";
				html += "\/* iPads (landscape) Styling *\/";
				html += "@media handheld, all and (device-width: 768px) and (device-height: 1024px) and (orientation : landscape) {";
				html += ".wrapper-ipad {";
				html += "	max-width: 280px !important;";
				html += "}";
				html += "}";
				html += "";
				html += "\/* iPads (portrait) Styling *\/";
				html += "@media handheld, all and  (device-width: 768px) and (device-height: 1024px) and (orientation : portrait) {";
				html += ".wrapper-ipad {";
				html += "	max-width: 280px !important;";
				html += "}";
				html += "}";
				html += "<\/style>";
				html += "<\/head>";
				html += "<body style=\"margin: 0 !important; padding: 0 !important;\">";
				html += "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\">";
				html += "  <tr>";
				html += "    <td align=\"center\">";
				html += "      <!--[if (gte mso 9)|(IE)]>";
				html += "      <table align=\"center\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"600\">";
				html += "      <tr>";
				html += "      <td align=\"center\" valign=\"top\" width=\"600\">";
				html += "      <![endif]-->";
				html += "      <table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"max-width: 600px;\" class=\"wrapper\">";
				html += "        <tr>";
				html += "          <td align=\"center\" height=\"25\" style=\"height:25px; font-size: 0;\">&nbsp;<\/td>";
				html += "        <\/tr>";
				html += "        <tr>";
				html += "          <td align=\"center\" valign=\"bottom\" style=\"font-size: 11px; font-family: Helvetica, Arial, sans-serif; color: #2C3E50;\"> Taiga Special Offer | <a href=\"http:\/\/www.htmlemailcheck.com\" title=\"Online Version\" target=\"_blank\" style=\"color:#26d0ae; text-decoration: none;\">Online Version<\/a> <\/td>";
				html += "        <\/tr>";
				html += "        <tr>";
				html += "          <td align=\"center\" height=\"25\" style=\"height:25px; font-size: 0;\">&nbsp;<\/td>";
				html += "        <\/tr>";
				html += "        <tr>";
				html += "          <td align=\"center\" height=\"25\" style=\"height:25px; font-size: 0;\">&nbsp;<\/td>";
				html += "        <\/tr>";
				html += "      <\/table>";
				html += "      <!--[if (gte mso 9)|(IE)]>";
				html += "      <\/td>";
				html += "      <\/tr>";
				html += "      <\/table>";
				html += "      <![endif]-->";
				html += "      <\/td>";
				html += "  <\/tr>";
				html += "  <tr>";
				html += "    <td bgcolor=\"#ffffff\" align=\"center\" style=\"padding: 0 10px 0 10px;\">";
				html += "      <!--[if (gte mso 9)|(IE)]>";
				html += "      <table align=\"center\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\" width=\"600\">";
				html += "      <tr>";
				html += "      <td align=\"center\" valign=\"top\" width=\"600\">";
				html += "      <![endif]-->";
				html += "      <table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" width=\"100%\" style=\"max-width: 600px;\" class=\"table-max\">";
				html += "        <tr>";
				html += "          <td><table width=\"100%\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\">";
				html += "              <tr>";
				html += "                <td align=\"center\">";
				html += "                <a href=\"http:\/\/www.htmlemailcheck.com\" title=\"Replace with your text\" target=\"_blank\">";
				html += "                	<img src=\"https:\/\/i.imgur.com\/negSNFS.png\" width=\"100%\" border=\"0\" alt=\"Replace with your text\" style=\"display: block; border:0; width:100%; height:auto !important;\" class=\"img-max\">";
				html += "                <\/a>";
				html += "              <\/td>";
				html += "              <\/tr>";
				html += "            <\/table><\/td>";
				html += "        <\/tr>";
				html += "      <\/table>";
				html += "      <!--[if (gte mso 9)|(IE)]>";
				html += "      <\/td>";
				html += "      <\/tr>";
				html += "      <\/table>";
				html += "      <![endif]-->";
				html += "      <\/td>";
				html += "  <\/tr>";
				html += "  <\/table>";
				html += "  <\/td>  ";
				html += "  <\/tr>";
				html += "<\/table>";
				html += "<\/body>";
				html += "<\/html>";



		     	// create reusable transporter object using the default SMTP transport 
				var transporter = nodemailer.createTransport({
				        service: 'Gmail',
				        auth: {
				            user: 'Taiga.user1@gmail.com', // Your email id
				            pass: 'bananaman' // Your password
				        }
				    });

		     	var mailOptions = {
				    from: '"Taiga 👥" <coupons@Taiga.com>', // sender address 
				    to: 'Kenny Rivers, Taiga.user1@gmail.com', // list of receivers 
				    subject: 'Special Offer!!', // Subject line 
				    html: html // html body 
				};
				 
				// send mail with defined transport object 
				transporter.sendMail(mailOptions, function(error, info){
				    if(error){
				    	console.log(error)
				        return res.status(400).send({message: error})
				    }
				    return res.status(200).send({message: JSON.stringify(response.body)});
				});
		     }
   		});
	}
}