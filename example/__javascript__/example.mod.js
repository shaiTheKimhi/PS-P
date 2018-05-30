	(function () {
		var __name__ = '__main__';
		var f = function () {
			alert ('123');
		};
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.f = f;
		__pragma__ ('</all>')
	}) ();
