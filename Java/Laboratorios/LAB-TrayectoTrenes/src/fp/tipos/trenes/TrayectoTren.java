package fp.tipos.trenes;

import java.time.Duration;
import java.time.LocalTime;
import java.util.Set;

public interface TrayectoTren{
	String getCodigoTren();
	String getNombreTrayecto();
	TipoTren getTipoTren();
	Set<Parada> getParadas();
	LocalTime getHoraSalida();
	LocalTime getHoraLlegada();
	Duration getDuracion();
	LocalTime getHoraSalida(String estacion);
	LocalTime getHoraLlegada(String estacion);
	void anyadirEstacionIntermedia(int posicion,
			String estacion,
			LocalTime horaLlegada,
			LocalTime horaSalida);
	void eliminarEstacionIntermedia(String estacion);
}
