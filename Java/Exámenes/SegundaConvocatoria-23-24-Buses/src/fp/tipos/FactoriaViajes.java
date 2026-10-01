package fp.tipos;

import java.time.Duration;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import fp.utiles.Checkers;

public class FactoriaViajes {
	private static Viaje parsearViaje(String linea) {
		Checkers.checkNoNull(linea);
		String [] trozos = linea.split(";");
		Checkers.check("Formato no válido->" + trozos.length, trozos.length == 5);
		Double precio = Double.parseDouble(trozos[0].trim());
		Integer distancia = Integer.parseInt(trozos[1].trim());
		Duration duracion = parsearDuracion(trozos[2].trim());
		TipoViaje tipo = TipoViaje.valueOf(trozos[3].trim().toUpperCase());
		List<Parada> trayecto = parsearTrayecto(trozos[4].trim());
		return new Viaje(precio, distancia, duracion, tipo, trayecto);
		}
	
	private static Duration parsearDuracion(String strDuracion) {
		Checkers.checkNoNull(strDuracion);
		String [] trozos = strDuracion.split(":");
		Checkers.check("Formato no válido", trozos.length == 2);
		Integer horas = Integer.parseInt(trozos[0].trim());
		Integer minutos = Integer.parseInt(trozos[1].trim());
		return Duration.ofHours(horas).plusMinutes(minutos);
		}
	
	private static List<Parada> parsearTrayecto(String strTrayecto) {
		String limpia = strTrayecto.replace("[", "").replace("]","");
		String [] trozos = limpia.split(",");
		Checkers.check("Formato no válido->" + trozos.length + "-->" +
		Arrays.toString(trozos), trozos.length >= 2);
		List<Parada> res = Arrays.stream(trozos)
				.map(FactoriaViajes::parseaParada)
				.collect(Collectors.toList());
		return res;
		}
	
	private static Parada parseaParada(String strParada) {
		String [] trozos = strParada.split("-");
		String parada = trozos[0].trim();
		String strHora =trozos[1].trim();
		LocalTime hora = null;
		if (!strHora.toUpperCase().equals("FIN")) {
			hora = parseaHora(strHora);
			}
		return new Parada(parada, hora);
		}
	
	private static LocalTime parseaHora(String strHora) {
		return LocalTime.parse(strHora, DateTimeFormatter.ofPattern("HH:mm"));
		}
	
	public static AgenciaBus leerViajes(String string, String string2) {
		return null;
	}
}