package fp.asociacion;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

import fp.utiles.Checkers;

public class FactoriaRevistas {
	
	private static final String SEPARADOR_PRINCIPAL = ";";
	private static final String SEPARADOR_ARTICULOS = ",";
	private static final String SEPARADOR_ARTICULO = "-";
	
	
	public static Revista parseaRevista(String revistaStr) {
		Checkers.checkNoNull(revistaStr);
		String [] trozos = revistaStr.split(SEPARADOR_PRINCIPAL);
		Checkers.check("Formato no válido <" + revistaStr + ">"
				, trozos.length == 6);
		
		String numero = trozos[0].trim();
		LocalDate fechaPublicacion = LocalDate.parse(trozos[1].trim()
				,DateTimeFormatter.ofPattern("d/M/y"));
		Integer ejemplares = Integer.valueOf(trozos[2].trim());
		Integer paginasFija = Integer.valueOf(trozos[3].trim());
		Integer anuncios = Integer.valueOf(trozos[4].trim());
		List<Articulo> articulos = parseaArticulos(trozos[5].trim());
		
		return new Revista(numero, fechaPublicacion, 
				ejemplares, paginasFija, anuncios, articulos);
	}
	
	public static List<Articulo> parseaArticulos(String articulosStr) {
		articulosStr = articulosStr.replace("[", "").replace("]", "");
		String [] trozos = articulosStr.split(SEPARADOR_ARTICULOS);
		List<Articulo> res = new ArrayList<>();
		for (String t : trozos) {
			res.add(parseaArticulo(t.trim()));
		}
		return res;		
	}
	
	private static Articulo parseaArticulo(String articuloStr) { 
		String [] trozos = articuloStr.split(SEPARADOR_ARTICULO); 
		Checkers.check("Formato de artículo no válido <"+articuloStr+">", 
				trozos.length == 3); 
		String titulo = trozos[0].trim(); 
		String categoria = trozos[1].trim(); 
		Integer paginas = Integer.valueOf(trozos[2].trim()); 
		return new Articulo(titulo, categoria, paginas); 
		}
}
