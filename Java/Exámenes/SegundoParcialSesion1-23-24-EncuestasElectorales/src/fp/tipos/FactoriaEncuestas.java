package fp.tipos;

import java.nio.charset.StandardCharsets;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import fp.utiles.Checkers;
import fp.utiles.Ficheros;

public class FactoriaEncuestas {
	public static Encuesta parsearEncuesta(String lineaCSV) {
		Checkers.checkNoNull(lineaCSV);
		String [] trozos = lineaCSV.split(",");
		Checkers.check("FactoriaEncuestas::Formato no válido", trozos.length == 8);
		String nombre = trozos[0].strip();
		LocalDate fechaComienzo = LocalDate.parse(trozos[1].trim(), 
				DateTimeFormatter.ofPattern("yyyy-mm-DD"));
		LocalDate fechaFin = LocalDate.parse(trozos[2].trim(), 
				DateTimeFormatter.ofPattern("yyyy-mm-DD"));
		Integer numeroEncuestados = Integer.valueOf(trozos[3].trim());
		String pais = trozos[4].trim();
		TipoEncuesta tipoEncuesta = TipoEncuesta.valueOf(trozos[5].trim().toUpperCase());
		Double porcentajeIndecisos = Double.valueOf(trozos[6].trim());
		List<Resultado> resultados = parseaResultados(trozos[7].trim());
		
		
		return new Encuesta(nombre, fechaComienzo, fechaFin, numeroEncuestados, pais, tipoEncuesta, porcentajeIndecisos, resultados);
	}
	
	private static List<Resultado> parseaResultados(String StrResultados) {
		Checkers.checkNoNull(StrResultados);
		List<Resultado> resultados = new ArrayList<>();
		String StrResultadosNuevos = StrResultados.replace("'", "");
		String [] trozos = StrResultadosNuevos.split(";");
		for (String trozo : trozos) {
			resultados.add(parseaResultado(trozo));
		}
		return resultados;
	}

	private static Resultado parseaResultado(String trozo) {
		Checkers.checkNoNull(trozo);
		String trozoNuevo = trozo.replace("(", "").replace(")", "");
		String [] lineas = trozoNuevo.split(":");
		String partido = lineas[0].trim();
		Double porcentaje = Double.valueOf(lineas[1].trim());
		return new Resultado(partido, porcentaje);
	}
	
	public static List<Encuesta> leeEncuestas(String fichero) {
		Checkers.checkNoNull(fichero);
		String errMsg = String.format("Error leyendo el fichero <%s>", 
				fichero);
		List<String> lineas = Ficheros.leeFichero(errMsg, 
				fichero,
				StandardCharsets.UTF_8);
		
		List<Encuesta> encuestas = lineas.stream()
				.skip(1)
				.map(linea -> parsearEncuesta(linea))
				.collect(Collectors.toList());
		return encuestas;
	}
}
