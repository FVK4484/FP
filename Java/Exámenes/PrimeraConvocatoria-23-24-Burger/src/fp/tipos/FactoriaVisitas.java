package fp.tipos;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import fp.utiles.Checkers;

public class FactoriaVisitas {
	
	private static Visita parseaVisita(String lineaCSV) {
		Checkers.checkNoNull(lineaCSV);
		String [] trozos = lineaCSV.split(";");
		Checkers.check("FactoriaVisitas::Formato no válido", trozos.length == 7);
		String email = trozos[0].strip();
		String ciudad = trozos[1].strip();
		String cp = trozos[2].strip();
		LocalDateTime entrada = LocalDateTime.parse(trozos[3].strip(),
		DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
		Double temperatura = Double.valueOf(trozos[4].strip());
		LocalDateTime salida = LocalDateTime.parse(trozos[5].strip(),
		DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
		List<Evaluacion> evaluaciones = parseaEvaluaciones(trozos[6].trim());
		return new Visita(email, ciudad, cp, entrada, salida, temperatura, evaluaciones);
	}
	
	private static List<Evaluacion> parseaEvaluaciones(String cad) {
		String clean = cad.replace("[","").replace("]", "");
		String [] trozos = clean.split("-");
		List<Evaluacion> res = new ArrayList<>();
		for (String trozo:trozos) {
			res.add(parseaEvaluacion(trozo.strip()));	
		}
		return res;
	}
	
	private static Evaluacion parseaEvaluacion(String trozo) {
		String clean = trozo.replace("(","").replace(")", "");
		String [] trozos = clean.split(":");
		Checkers.check("Formato evaluación no válido", trozos.length == 2);
		String nombre = trozos[0].trim();
		String[] puntuacionesStr = trozos[1].split(",");
		Checkers.check("Puntuaciones incorrectas", puntuacionesStr.length == 4);
		Integer presentacion = Integer.valueOf(puntuacionesStr[0].trim());
		Integer punto = Integer.valueOf(puntuacionesStr[1].trim());
		Integer ingredientes = Integer.valueOf(puntuacionesStr[2].trim());
		Integer pan = Integer.valueOf(puntuacionesStr[3].trim());
		return new Evaluacion(nombre, presentacion, punto, ingredientes, pan);
	}

	public static Competicion leeCompeticion(String ruta) {
		return null;
	}
}	

