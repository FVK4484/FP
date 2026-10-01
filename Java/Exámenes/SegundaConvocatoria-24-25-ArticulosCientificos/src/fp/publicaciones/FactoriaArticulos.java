package fp.publicaciones;

import java.nio.charset.StandardCharsets;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.stream.Collectors;
import fp.utiles.Checkers;
import fp.utiles.Ficheros;

public class FactoriaArticulos {
	
	private static Articulo parseaArticulo(String lineaCSV) {
		Articulo res = null;
		Checkers.checkNoNull(lineaCSV);
		String [] trozos = lineaCSV.split(",");
		Checkers.check("FactoriaArticulos :: Formato no válido", trozos.length == 7);
		String titulo = trozos[0].strip();
		List<Autor> autores = parseaAutores(trozos[1].strip());
		LocalDate fechaPublicacion = LocalDate.parse(trozos[2].strip()
				, DateTimeFormatter.ofPattern("yyyy/MM/dd"));
		String revista = trozos[3].strip();
		TipoPublicacion tipoPublicacion = TipoPublicacion.
				valueOf(trozos[4].toUpperCase().strip());
		Integer numeroCitas = Integer.valueOf(trozos[5].strip());
		SortedSet<String> keywords = parseaKeywords(trozos[6].strip());
		
		if (trozos.length == 7) { 
			res = new Articulo(titulo, autores, fechaPublicacion, revista, tipoPublicacion); 
		} else if (trozos.length == 8){
			Double precio = Double.parseDouble(trozos[7].strip()); 
			res = new ArticuloPago(titulo, autores, fechaPublicacion, revista, precio); 
		} res.setNumeroCitas(numeroCitas); 
		for (String keyword: keywords) { 
			res.agregaKeyword(keyword); 
		} return res;
	}
	
	private static List<Autor> parseaAutores(String autoresStr) {
		List<Autor> autores = new ArrayList<>();
		String [] lineas = autoresStr.split(";");
		for (String linea : lineas) {
			autores.add(parseaAutor(linea));
		}
		return autores;
	}
	
	private static Autor parseaAutor(String autorStr) {
		String [] cachos = autorStr.split("-");
		Checkers.check("Formato no válido", cachos.length==2);
		String nombre = cachos[0].strip();
		String afiliacion = cachos[1].strip();
		Boolean correspondencia = false;
		if (nombre.startsWith("*")) {
			correspondencia = true;
			nombre.replace("*", "");
		}
		return new Autor(nombre, afiliacion, correspondencia);
	}
	
	private static SortedSet<String> parseaKeywords(String keywordsStr) { 
		String [] trozos= keywordsStr.split(";"); 
		SortedSet<String> ss = new TreeSet<>(); 
		for (String trozo:trozos) { 
			ss.add(trozo.strip()); 
		} return ss; 
	} 
	
	public static List<Articulo> leeArticulos(String fichero) {
		Checkers.checkNoNull(fichero);
		String errMsg = String.format("Error leyendo fichero <%s>", fichero);
		List<String> lineas = Ficheros.leeFichero(errMsg, fichero, StandardCharsets.UTF_8);

		List<Articulo> res = lineas.stream()
				                  .skip(1)
				                  .map(linea -> parseaArticulo(linea))
				                  .collect(Collectors.toList());
		return res;
	}

}