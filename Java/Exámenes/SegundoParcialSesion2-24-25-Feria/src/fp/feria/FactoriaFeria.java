package fp.feria;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;


import fp.utiles.Checkers;
import fp.utiles.Ficheros;

public class FactoriaFeria {
	
	private static final String SEPARADOR_PRINCIPAL = ";";
	private static final String SEPARADOR_MENU = ","; 
	private static final String SEPARADOR_PRODUCTO = "-"; 
	
	//EL 88 DE COSTILLARES;publica;113;150;rebujito - 7.5 , tortilla patatas - 10 , jamon - 20;flamenco;si;87 
	
	public static CasetaFeria parseaCaseta(String casetaStr) { 
		
		Checkers.checkNoNull(casetaStr); 
		String [] trozos = casetaStr.split(SEPARADOR_PRINCIPAL); 
		Checkers.check("Formato no válido <"+casetaStr+">", trozos.length == 8); 
		String nombre = trozos[0].trim(); 
		TipoCaseta tipo = parseaTipo(trozos[1].trim()); 
		Integer modulo = Integer.parseInt(trozos[2].trim()); 
		Integer aforo = Integer.parseInt(trozos[3].trim()); 
		Set<Producto> menu = parseaMenu(trozos[4].trim()); 
		String musica = trozos[5].trim(); 
		Boolean adaptado = parseaAdaptado(trozos[6].trim()); 
		Double valoracion = Double.parseDouble(trozos[7].trim()); 
		return new CasetaFeria(nombre, tipo, modulo, aforo,menu, musica, adaptado, valoracion); 
		
	}
	
	private static Boolean parseaAdaptado(String adaptadoStr) { 
		
		Boolean res = null; 
		adaptadoStr = adaptadoStr.toLowerCase(); 
		if (adaptadoStr.equals("si")) { 
			res = true; 
		} else if (adaptadoStr.equals("no")) {
			res = false; 
		} 
		return res; 
		
	} 
	
	private static Set<Producto> parseaMenu(String menuStr) { 
		
		String [] trozos = menuStr.split(SEPARADOR_MENU); 
		Set<Producto> res = new HashSet<>(); 
		for (String trozo: trozos) {
			res.add(parseaProducto(trozo.trim())); 
		} 
		return res; 
		
	} 
	
	private static Producto parseaProducto(String productoStr) {
		
		String [] trozos = productoStr.split(SEPARADOR_PRODUCTO); 
		Checkers.check("Formato producto no válido <"+productoStr+">", trozos.length == 2); 
		String nombre = trozos[0].trim(); 
		Double precio = Double.parseDouble(trozos[1].trim()); 
		return new Producto(nombre, precio); 
		
	} 
	
	private static TipoCaseta parseaTipo(String tipoStr) { 
		return TipoCaseta.valueOf(tipoStr.toUpperCase()); 
	}
	
	public static Set<CasetaFeria> leeCasetas(String ficheroCSV) {
		Checkers.checkNoNull(ficheroCSV);
		String errMsg = String.format("Error leyendo fichero <%s>", ficheroCSV);
		List<String> lineas = Ficheros.leeFichero(errMsg, ficheroCSV);
		return lineas.stream()
				.skip(1)
				.map(c -> parseaCaseta(c))
				.collect(Collectors.toSet());
	}
	
}
