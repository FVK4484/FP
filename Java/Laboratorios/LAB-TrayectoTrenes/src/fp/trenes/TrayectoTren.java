package fp.trenes;

import java.time.Duration;
import java.time.LocalTime;
import java.util.List;

public interface TrayectoTren {
	
	public String getCodigo();
	public String getNombreTrayecto();
	public TipoTren getTipo();
	public List<String> getEstaciones();
	public List<LocalTime> getHorasSalida();
	public List<LocalTime> getHorasLlegada();
	
	public LocalTime getHoraSalida();
	public LocalTime getHoraLlegada();
	public Duration getDuracionTrayecto();
	
	LocalTime getHorasSalida(String estacion);
	LocalTime getHorasLlegada(String estacion);
	void anadirEstacionIntermedia(int posicion, String estacion, 
			LocalTime horaLlegada, LocalTime horaSalida);
	void eliminarEstacionIntermedia(String estacion); 

}
