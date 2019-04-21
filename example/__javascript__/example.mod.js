	(function () {
		var __name__ = '__main__';
		var f = function () {
			var a = prompt ('enter message');
			alert (a);
		};
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.f = f;
		__pragma__ ('</all>')
	}) ();
