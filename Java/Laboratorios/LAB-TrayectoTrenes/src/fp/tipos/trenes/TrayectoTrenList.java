package fp.tipos.trenes;

import java.time.Duration;
import java.time.LocalTime;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import fp.utiles.Checkers;

public class TrayectoTrenList implements TrayectoTren{
	private String codigoTren, nombreTrayecto;
	private TipoTren tipoTren;
	private List<Parada> listaParadas;
	
	public String getCodigoTren() {
		return codigoTren;
	}

	public String getNombreTrayecto() {
		return nombreTrayecto;
	}

	public TipoTren getTipoTren() {
		return tipoTren;
	}

	public Set<Parada> getParadas() {
		return new HashSet<>(listaParadas);
	}

	public LocalTime getHoraSalida() {
		Parada inicio = listaParadas.get(0);
		return inicio.horaSalida();
	}

	public LocalTime getHoraLlegada() {
		Parada inicio = listaParadas.getLast();
		return inicio.horaLlegada();
	}

	public Duration getDuracion() {
		return Duration.between(getHoraSalida(), getHoraLlegada());
	}
	
	private Integer buscaEstacion(String estacion) {
		Integer result = -1;
		for (int i = 0; i < listaParadas.size(); i++) {
			Parada parada = listaParadas.get(i);
			if (parada.nombre().equals(estacion)) {
				result = i;
				break;
			}
		}
		return result;
	}

	public LocalTime getHoraSalida(String estacion) {
		LocalTime result = null;
		Integer posicion = buscaEstacion(estacion);
		if (posicion != -1 && posicion != listaParadas.size() - 1) {
			result = listaParadas.get(posicion).horaSalida();
		}
		return result;
	}

	public LocalTime getHoraLlegada(String estacion) {
		LocalTime result = null;
		Integer posicion = buscaEstacion(estacion);
		if (posicion != -1 && posicion != 0) {
			result = listaParadas.get(posicion).horaLlegada();
		}
		return result;
	}
	
//	1.
//	Si la posición no es intermedia 
//	(debe ser mayor o igual que 1 y menor 
//			que el número de paradas).
//	2.
//	Si la hora de salida es anterior a la 
//	hora de llegada.
//	3.
//	Si la hora de llegada es anterior a la 
//	hora de salida de la parada anterior.
//	4.
//	Si la hora de salida es posterior a la 
//	hora de llegada de la parada siguiente.

	public void anyadirEstacionIntermedia(int posicion, 
			String estacion, LocalTime horaLlegada, 
			LocalTime horaSalida) {
		Checkers.check("La posición no es intermedia.", 
				posicion >= 0 && posicion < listaParadas.size());
		Checkers.check("Hora salida no puede ser anterior a hora llegada.", 
				!horaSalida.isBefore(horaLlegada));
		Parada anterior = listaParadas.get(posicion - 1);
		Checkers.check("Parada con hora de llegada anterior a la salida en parada anterior", 
				!horaLlegada.isBefore(anterior.horaSalida()));
		Parada posterior = listaParadas.get(posicion);
		Checkers.check("Parada con hora de salida posterior a la llegada en parada siguiente", 
				!horaSalida.isAfter(posterior.horaLlegada()));
		Parada p = new Parada(estacion, horaLlegada, horaSalida);
		listaParadas.add(posicion, p);
	}

	public void eliminarEstacionIntermedia(String estacion) {
		Integer posicion = buscaEstacion(estacion);
		Checkers.check("Posición no válida (primera, última, no pertenece",
				posicion != 0 && posicion != listaParadas.size() - 1 && posicion != -1);
		listaParadas.remove(posicion);
	}
	
	
	
}
