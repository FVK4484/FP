package fp.tipos;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

import fp.utiles.Checkers;

public class FactoriaJugadores {
	
	public Jugador parsearJugador(String lineaCSV) {
		Checkers.checkNoNull(lineaCSV);
		String [] trozos = lineaCSV.split(";");
		Checkers.check("Formato no válido", trozos.length == 8);
		String nombre = trozos[0].trim();
		LocalDate fechaNacimiento = LocalDate.parse(trozos[1].trim(), 
				DateTimeFormatter.ofPattern("yyyy-MM-dd"));
		TipoPosicion tipoPosicion = TipoPosicion.valueOf(trozos[2].trim().toUpperCase());
		Integer goles = Integer.valueOf(trozos[3].trim());
		Integer asistencias = Integer.valueOf(trozos[4].trim());
		List<String> lesiones = parsearLesiones(trozos[5].trim());
		String club = trozos[6].trim();
		Integer clasificacion = Integer.valueOf(trozos[7].trim());
		String estadio = trozos[8].trim();
		return new Jugador(nombre, fechaNacimiento, tipoPosicion, goles, asistencias, new Equipo(club, clasificacion, estadio), lesiones);
	}

	private List<String> parsearLesiones(String lesionesStr) {
		List<String> res = new ArrayList<>();
		if (lesionesStr.length() >= 1) {
			String lesionesStrNuevo = lesionesStr.replace("[", "").replace("]", "");
			for (String lesion : lesionesStrNuevo.split(",")) {
				res.add(lesion);
			}
		} else if (lesionesStr.length() == 1) {
			String lesionesStrNuevo = lesionesStr.replace("[", "").replace("]", "");
			res.add(lesionesStrNuevo);
		} 
		return res;
	}
	
}
