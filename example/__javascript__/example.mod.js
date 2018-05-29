	(function () {
		var __name__ = '__main__';
		var chain = __init__ (__world__.itertools).chain;
		var greet = function (self) {
			self.planet = self.planets [int (Math.random () * len (self.planets))];
			document.getElementById ('greet').innerHTML = 'Hello {}'.format (self.planet [0]);
		};
		var explain = function (self) {
			document.getElementById ('explain').innerHTML = '123';
		};
		__pragma__ ('<use>' +
			'itertools' +
		'</use>')
		__pragma__ ('<all>')
			__all__.__name__ = __name__;
			__all__.chain = chain;
			__all__.explain = explain;
			__all__.greet = greet;
		__pragma__ ('</all>')
	}) ();
