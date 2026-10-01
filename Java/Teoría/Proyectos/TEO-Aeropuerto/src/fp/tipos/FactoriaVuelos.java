package fp.tipos;

import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import fp.utiles.Checkers;
import fp.utiles.Ficheros;

public class FactoriaVuelos {
	
	private static Vuelo parseaVuelo(String datosVuelo) {
		
		Checkers.checkNoNull(datosVuelo);
		String [] trozos = datosVuelo.split(";");
		if (trozos.length != 9) {
			throw new IllegalArgumentException("Formato de vuelo no válido");	
		}
		String origen = trozos[0].strip();
		String destino = trozos[1].strip();
		Trayecto trayecto = new Trayecto(origen, destino);
		Double precio = Double.valueOf(trozos[2].strip());
		Integer numPasajeros = Integer.valueOf(trozos[3].strip());
		Integer numPlazas = Integer.valueOf(trozos[4].strip());
		String codigo = trozos[5].strip();
		LocalDate fecha = parseaFecha(trozos[6].strip());
		Duration duracion = parseaDuracion(trozos[7].strip());
		List<String> tripulacion = parseaTripulacion(trozos[8].strip());
		return new Vuelo(trayecto, precio, numPasajeros, numPlazas, codigo, fecha, duracion, tripulacion);
	
	}
	
	private static LocalDate parseaFecha(String fecha) {
		
		return LocalDate.parse(fecha.strip()
				,DateTimeFormatter.ofPattern("dd/MM/yyyy"));
		
	}
	
	private static Duration parseaDuracion(String duracion) {
		
		Long minutos = Long.valueOf(duracion.strip());
		return Duration.ofMinutes(minutos);
		
	}
	
	private static List<String> parseaTripulacion(String tripulacion) {
		
		Checkers.checkNoNull(tripulacion);
		String [] lineas = tripulacion.split(",");
		Integer i = 0;
		List<String> listaTripulacion = new ArrayList<>();
		for (i = 0; i < lineas.length; i++) {
			listaTripulacion.add(lineas[i]);
		}
		return listaTripulacion;	
		
	}
	
//	public static List<Vuelo> leeVuelos(String fichero) {
//	    List<Vuelo> res = new ArrayList<>();
//
//	    try {
//	        List<String> lineas = Files.readAllLines(Paths.get(fichero));
//	        lineas.remove(0);
//	        for (String linea : lineas) {
//	            Vuelo v = parseaVuelo(linea);
//	            res.add(v);
//	        }
//	    } catch (IOException e) {
//	        System.out.println("No se ha encontrado el fichero");
//	        e.printStackTrace();
//	    }
//	    return res;
//	}
	
	public static List<Vuelo> leeVuelos(String fichero) {
		Checkers.checkNoNull(fichero);
		String errMsg = String.format("Error leyendo fichero <%s>"
				, fichero);
		List<String> lineas = Ficheros.leeFichero(errMsg, fichero, StandardCharsets.UTF_8);

		List<Vuelo> res = lineas.stream()
				                  .skip(1)
				                  .map(linea -> parseaVuelo(linea))
				                  .collect(Collectors.toList());
		return res;
		
	}
	
}
