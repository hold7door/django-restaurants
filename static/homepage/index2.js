			(function(yourcode){

							// The global jQuery object is passed as a parameter
							yourcode(window.jQuery, window, document);

				  }(function($, window, document) {

							// The $ is now locally scoped 

						   // Listen for the jQuery ready event on the document
						   
						   $(function() {
							$('.a').hide();
					
							$('.hello').hide();
							 // The DOM is ready!
							$( window ).resize(function() {
								if($(window).width() < 1300){
									$('.left').hide();
								}else{
									$('.left').show();
								}
								if($(window).width() < 980){
									$('.right').hide();
									$('.rr').removeClass('centered');
								}else{
									$('.right').show();
									$('.rr').addClass('centered');
								}
							});
						 });

						   // The rest of the code goes here!}
			}));
			var b = 1; 
			var eleT = null;
			function clicke(i){ 
						$(i).hide();
						var pare = i.parentNode;
						var ele = pare.querySelector('.hello');
						var ele2 = pare.querySelector('.hell');
						var eleA = pare.querySelector('.adda');
						var eleCount = getCount(ele);
									if(eleCount <= 6)
									{
										$(pare).toggleClass('clicked1');
									}else if(eleCount <= 9)
									{
										$(pare).toggleClass('clickeda1');
										$(ele).addClass('clicked2');
									}else if(eleCount <= 11)
									{
										$(pare).toggleClass('clickedb1');
										$(ele).addClass('clickeda2');
									}else if(eleCount <= 13)
									{
										$(pare).toggleClass('clickedc1');
										$(ele).addClass('clickedb2');
									}else{
										$(pare).toggleClass('clickedd1');
										$(ele).addClass('clickedc2');
									}	
										var text = $(i).text();
										$(i).text((text == 'See More') ? 'See Less' : 'See More');
										$(i).toggleClass('spll');
										if($(ele2).hasClass('visible')){
											$(ele2).removeClass('visible');
											$(ele2).addClass('invisible');
											$(ele2).fadeOut();
											$(eleA).fadeIn();
											$(ele).fadeIn();
										}else{
											$(ele2).removeClass('invisible');
											$(ele2).addClass('visible');
											$(ele2).fadeIn();
											$(eleA).fadeOut();
											$(ele).fadeOut();
										}
		
									//$('#meddiv').show();
									$(i).fadeIn(1000);
							}
			function sh(i2){
				$(i2).show();
			}
			function getCount(parent){
						var relevantChildren = 0;
						var children = parent.childNodes.length;
						for(var i=0; i < children; i++){
							if(parent.childNodes[i].nodeType != 3){
								relevantChildren++;
							}
						}
						return relevantChildren;
			}
				