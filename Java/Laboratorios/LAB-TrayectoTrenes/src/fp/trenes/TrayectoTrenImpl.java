package fp.trenes;

import java.time.Duration;
import java.time.LocalTime;
import java.util.LinkedList;
import java.util.List;
import fp.utiles.Checkers;

public class TrayectoTrenImpl implements TrayectoTren {
	
	 // Atributos
	
	private String codigo;
	private String nombreTrayecto;
	private TipoTren tipo;
	private List<String> estaciones;
	private List<LocalTime> horasSalida;
	private List<LocalTime> horasLlegada;
	
	// Constructor
	
	public TrayectoTrenImpl(String codigo, String nombreTrayecto, TipoTren tipo, 
			String origen, String destino, LocalTime horaSalida, LocalTime horaLlegada) {
		
		super();
		
		Checkers.checkNoNull(horaSalida, horaLlegada);
		
		this.codigo = codigo;
		this.nombreTrayecto = nombreTrayecto;
		this.tipo = tipo;
		this.estaciones = new LinkedList<>();
		estaciones.add(origen); estaciones.add(destino);
		this.horasSalida = new LinkedList<>();
		horasSalida.add(horaSalida); horasSalida.add(null);
		this.horasLlegada= new LinkedList<>();
		horasLlegada.add(null); horasLlegada.add(horaLlegada);
	}
	
	@Override
	public String getCodigo() {
		return  codigo;
	}

	@Override
	public String getNombreTrayecto() {
		return nombreTrayecto;
	}

	@Override
	public TipoTren getTipo() {
		return tipo;
	}

	@Override
	public List<String> getEstaciones() {
		return new LinkedList<>(estaciones);
	}

	@Override
	public List<LocalTime> getHorasSalida() {
		return new LinkedList<>(horasSalida);
	}

	@Override
	public List<LocalTime> getHorasLlegada() {
		return new LinkedList<>(horasLlegada);
	}

	@Override
	public LocalTime getHoraSalida() {
		return horasSalida.get(0);
	}

	@Override
	public LocalTime getHoraLlegada() {
		// return horasLlegada.get(horasLlegada.size()-1);
		return horasLlegada.getLast();
	}

	@Override
	public Duration getDuracionTrayecto() {
		return Duration.between(getHoraSalida(), getHoraLlegada());
	}

	@Override
	public LocalTime getHorasSalida(String estacion) {
		Integer posicion = estaciones.indexOf(estacion);
		return horasSalida.get(posicion);
	}

	@Override
	public LocalTime getHorasLlegada(String estacion) {
		Integer posicion = estaciones.indexOf(estacion);
		return horasLlegada.get(posicion);
	}

	@Override
	public void anadirEstacionIntermedia(int posicion, String estacion, 
			LocalTime horaLlegada, LocalTime horaSalida) {
		estaciones.add(posicion, estacion);
		horasLlegada.add(posicion, horaLlegada);
		horasSalida.add(posicion, horaSalida);
	}

	@Override
	public void eliminarEstacionIntermedia(String estacion) {
		int posicion = estacion.indexOf(estacion);
		estaciones.remove(estacion);
		horasSalida.remove(posicion);
		horasLlegada.remove(posicion);
	}

}
