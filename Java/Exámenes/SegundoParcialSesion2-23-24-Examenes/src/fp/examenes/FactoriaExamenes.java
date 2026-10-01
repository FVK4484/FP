package fp.examenes;

import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import fp.utiles.Checkers;
import fp.utiles.Ficheros;

public class FactoriaExamenes {
	private static Examen parsearExamen(String lineaCSV) {
		Checkers.checkNoNull(lineaCSV);
		String [] trozos = lineaCSV.split(",");
		Checkers.check("Formáto de cadena incorrecto.", 
				trozos.length == 9);
		String asignatura = trozos[0].trim();
		Integer curso = Integer.valueOf(trozos[1].trim());
		LocalDateTime fechaHora = parsearFechaHora(trozos[2].trim(), trozos[3].trim());
		Duration duracion = Duration.ofMinutes(Integer.valueOf(trozos[4].trim()));
		TipoExamen tipoExamen = TipoExamen.valueOf(trozos[5].trim().toUpperCase());
		Integer asistencia = Integer.valueOf(trozos[6].trim());
		Boolean inscripcion = parsearInscripcion(trozos[7].trim());
		List<Aula> aulas = parsearAulas(trozos[8].trim());
		return new Examen(asignatura, curso, fechaHora, duracion, tipoExamen, asistencia, inscripcion, aulas);
	}

	private static LocalDateTime parsearFechaHora(String fechaSTR, 
			String horaSTR) {
		String fechaHoraSTR = fechaSTR + " " + horaSTR;
		LocalDateTime fechaHora = LocalDateTime.parse(fechaHoraSTR, DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
		return fechaHora;
	}
	
	private static Boolean parsearInscripcion(String inscripcionSTR) {
		Boolean res = true;
		if (inscripcionSTR.equals("No")) {
			res = false;
		}
		return res;
	}
	
	private static List<Aula> parsearAulas(String aulasSTR) {
		List<Aula> aulas = new ArrayList<>();
		String [] trozos = aulasSTR.split(";");
		for (String trozo : trozos) {
			String [] lineas = trozo.split("-");
			Checkers.check("Cadena incorrecta.", lineas.length == 2);
			Aula aula = new Aula(lineas[0].trim(), Integer.valueOf(lineas[1]));
			aulas.add(aula);
		}
		return aulas;
	}
	
	public static List<Examen> leeExamenes(String fichero) {
		Checkers.checkNoNull(fichero);
		String errMsg = String.format("Error leyendo fichero <%s>", fichero);
		List<String> lineas = Ficheros.leeFichero(errMsg, fichero, StandardCharsets.UTF_8);
		List<Examen> res = lineas.stream()
				.skip(1)
				.map(linea -> parsearExamen(linea))
				.collect(Collectors.toList());
		return res;
	}
}
