<!DOCTYPE html>
<html>
<head>
<title>ERP - Universidad Católica de Santa María</title>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/png" href="img/logo_ucsm.png">
<link rel="stylesheet" href="js/jquery-ui-1.12.1/jquery-ui.css">
<link rel="stylesheet" href="bootstrap4/css/bootstrap.min.css">
<link rel="stylesheet" href="bootstrap4/bootstrap-select.min.css">
<link rel="stylesheet" href="css/style.css?d=1">
<script src="js/jquery-3.1.1.min.js"></script>
<script src="js/jquery-ui-1.12.1/jquery-ui.js"></script>
<script src="bootstrap4/js/bootstrap.bundle.min.js"></script>
<script src="bootstrap4/bootstrap-select.min.js"></script>
<script src="js/java.js?d=1"></script>
<script>
   function f_BuscarUsuario(){
      loCodUsu = document.getElementById("modal_agregarTarea_cCodUsu");
      loParams = document.getElementById("modal_agregarTarea_buscarCodUsu");
      if (loParams.value.length < 4) {
         alert("DEBE INGRESAR AL MENOS 4 LETRAS PARA COMENZAR LA BÚSQUEDA");
      }
      var lcSend = "Id=BuscarUsuario&pcParams="+loParams.value;
      $.post("Pla1190.php",lcSend).done(function(p_cResult) {
         var laJson = JSON.parse(p_cResult);
         if (laJson.ERROR){
            alert(laJson.ERROR);
            loParams.focus();
         } else {
            loCodUsu.innerHTML = '';
            for (var i = 0; i < laJson.length; i++) {
               var option = document.createElement("option");
               option.text =  laJson[i].CCODUSU + ' - ' + laJson[i].CNRODNI + ' - ' + laJson[i].CNOMBRE;
               option.value = laJson[i].CCODUSU;
               loCodUsu.add(option);
            }
            loCodUsu.focus();
         }
      });
   }

   function f_AgregarTarea(){
      loIndice = document.getElementById("modal_agregarTarea_nIndice");
      loDescri = document.getElementById("modal_agregarTarea_cDescri");
      loInicio = document.getElementById("modal_agregarTarea_dInicio");
      loFinali = document.getElementById("modal_agregarTarea_dFinali");
      loCodUsu = document.getElementById("modal_agregarTarea_cCodUsu");
      var lcSend = "Id=AgregarTarea&paData[NINDICE]="+loIndice.value+
                                  "&paData[CDESCRI]="+loDescri.value+
                                  "&paData[DINICIO]="+loInicio.value+
                                  "&paData[DFINALI]="+loFinali.value+
                                  "&paData[CCODUSU]="+loCodUsu.value;
      $.post("Pla1190.php",lcSend).done(function(p_cResult) {
         alert(p_cResult);
         loIndice.value = 0;
         document.getElementById("detalleTareas").innerHTML = p_cResult;
      });
   }

   /*
   function f_RevisarOrden(p_nIndice){
      document.getElementById("p_nIndice").value = p_nIndice;
      document.getElementById("Id").value = "RevisarOrden";
      document.getElementById("oform").submit();
   }
   */

   $(document).ready(function () {
      $('#modal_agregarTarea').on('shown.bs.modal', function (e) {
         $('#modal_agregarTarea_cDescri').focus();
      });

      $('#modal_agregarTarea_buscarCodUsu').keydown(function (e) {
         if (e.keyCode == 13) {
            f_BuscarUsuario();
            return false;
         }
      });

      $('#modal_agregarTarea_btnAgregarTarea').keydown(function (e) {
         if (e.keyCode == 13) {
            f_AgregarTarea();
            return false;
         }
      });
   });
   
</script>
</head>
<body style="padding-bottom: 0">
<div id="header"></div>
<form action="Pla1190.php" method="post" id="oform">
<div class="container-fluid">
   <div class="alert alert-info mb-2 py-1" role="alert">PROGRAMACIÓN DE ACTIVIDADES Y PROYECTOS PARA EL PRÓXIMO PERIODO<div class="float-right">{$scNombre} / {$scDesCCo}</div></div>
   {if $snBehavior eq 0}
      <div class="input-group mb-3 justify-content-center">
         <div class="input-group-prepend"><span class="input-group-text alert-dark">PERIODO DE PLANEAMIENTO EN PROGRAMACIÓN</span></div>
         <input type="text" class="form-control col-lg-1 text-center" value="{$scPerPla}" readonly tabindex="-1">
      </div>
      <div class="input-group mb-1 justify-content-center">
         <div class="list-group col-lg-6 text-center">
            <button type="submit" name="Boton0" value="FUNCIONAMIENTO" class="list-group-item list-group-item-action">ACTIVIDADES DE FUNCIONAMIENTO</button>
            <button type="submit" name="Boton0" value="DESARROLLO" class="list-group-item list-group-item-action">PROYECTOS DE DESARROLLO</button>
         </div>   
      </div>
   {else if $snBehavior eq 1}
   <div class="alert alert-success text-center py-0 mb-2" role="alert">{$scDesTip}</div>
      <input type="hidden" name="Id" id="Id">
      <input type="hidden" name="p_nIndice" id="p_nIndice">
      <div class="table-responsive mh-70 mb-3">
         <table class="table table-sm table-hover text-11 table-bordered">
            <thead class="bg-coral-1">
               <tr class="text-center">
                  <th scope="col" colspan="11">ACTIVIDADES/PROYECTOS</th>
               </tr>
               <tr class="text-center">
                  <th scope="col">#</th>
                  <th scope="col">ID</th>
                  <th scope="col">DENOMINACIÓN</th>
                  <th scope="col">ESTADO</th>
                  <th scope="col">PRESUPUESTO</th>
                  <th scope="col"><img src="css/svg/edit-blue.svg" width="15" height="15"></th>
               </tr>
            </thead>
            <tbody>
               {$k = 0}
               {foreach from=$saIdActi item=i}
                  <tr class="text-center">
                     <th scope="row">{$k+1}</th>
                     <td>{$i['CIDACTI']}</td>
                     <td class="text-left">{$i['CDESCRI']}</td>
                     <td>{$i['CDESEST']}</td>
                     <td class="text-right">{$i['NPREEST']}</td>
                     <td class="p-0"><button type="button" value="{$k}" onclick="f_VerDetalleActividad(this.value);" tabindex="-1"><img src="css/svg/edit-blue.svg" width="20" height="20"></button></td>
                  </tr>
                  {$k = $k + 1}
               {/foreach}
            </tbody>
         </table>
      </div>
      <div class="input-group input-group-sm justify-content-center">
         <button type="submit" name="Boton1" value="NUEVO" class="btn btn-outline-primary col-lg-3 mx-2">NUEVA ACTIVIDAD/PROYECTO</button>
         <button type="submit" name="Boton1" value="SALIR" class="btn btn-danger col-lg-3 mx-2">SALIR</button>
      </div>
   {else if $snBehavior eq 2}
      <div class="alert alert-success text-center py-0 mb-2" role="alert">{$scDesTip}</div>
      <div class="form-group text-15 mb-2">
         <label class="mb-1">1. UNIDAD RESPONSABLE DE LA ACTIVIDAD</label>
         <input type="hidden" name="paData[CCENCOS]" value="{$saData['CCENCOS']}">
         <div class="w-100 pr-3"><input type="text" name="paData[CDESCCO]" value="{$saData['CDESCCO']}" class="form-control form-control-sm ml-3" required readonly tabindex="-1"></div>
      </div>
      <div class="form-group text-15 mb-2">
         <label class="mb-1">2. DENOMINACIÓN DE LA ACTIVIDAD</label>
         <div class="w-100 pr-3"><input type="text" name="paData[CDESCRI]" value="{$saData['CDESCRI']}" class="form-control form-control-sm ml-3 text-uppercase" required autofocus></div>
      </div>
      <div class="form-group text-15 mb-2">
         <label class="mb-1">3. OBJETIVO ESTRATÉGICO CON EL QUE ESTÁ ALINEADO LA ACTIVIDAD A REALIZARSE</label>
         <div class="w-100 pr-3">
            <select name="paData[CCODOBJ]" required class="selectpicker form-control form-control-sm ml-3" data-live-search="true">
               {foreach from=$saCodObj item=i}
                  <option value="{$i['CCODOBJ']}" {if $i['CCODOBJ'] eq $saData['CCODOBJ']} selected {/if}>{$i['CDESCRI']}</option>
               {/foreach}
            </select>
         </div>
      </div>
      <div class="form-group text-15 mb-2">
         <label class="mb-1">4. ENTREGABLES</label>
         <div class="w-100 pr-3"><input type="text" name="paData[CINDICA]" value="{$saData['CINDICA']}" class="form-control form-control-sm ml-3 text-uppercase" required></div>
      </div>
      <div class="form-group text-15 mb-1">
         <label class="mb-1">5. TAREAS A DESARROLLARSE PARA EL LOGRO DEL RESULTADO DE LA ACTIVIDAD (ESTRUCTURA DE DESCOMPOSICIÓN DEL TRABAJO)</label>
      </div>
      <div class="table-responsive mh-30 mb-0">
         <table class="table table-sm table-hover text-12 table-collapse mb-0 border-collapse">
            <thead class="bg-coral-1">
               <tr class="text-center py-0">
                  <th class="align-middle py-0" scope="row" rowspan="2" style="width: 2%">#</th>
                  <th class="align-middle py-0" scope="row" rowspan="2" style="width: 55%">TAREAS</th>
                  <th class="align-middle py-0" scope="row" colspan="2" style="width: 14%">CRONOGRAMA</th>
                  <th class="align-middle py-0" scope="row" rowspan="2" style="width: 25%">RESPONSABLE</th>
                  <th class="align-middle py-0" scope="row" rowspan="2" style="width: 2%"><img src="css/svg/edit-blue.svg" width="15" height="15"></th>
                  <th class="align-middle py-0" scope="row" rowspan="2" style="width: 2%"><img src="css/svg/x-red.svg" width="15" height="15"></th>
               </tr>
               <tr class="text-center py-0">
                  <th class="align-middle py-0" scope="row" style="width: 7%">INICIO</th>
                  <th class="align-middle py-0" scope="row" style="width: 7%">FINALIZACIÓN</th>
               </tr>
            </thead>
            <tbody id="detalleTareas" class="text-13">
               {if $saTareas eq NULL}
                  <tr>
                     <td colspan="7" class="text-center">SIN TAREAS DEFINIDAS</td>
                  </tr>
               {else}
                  {$k = 0}
                  {foreach from=$saTareas item=i}
                     <tr>
                        <th class="text-right" scope="row">{$k+1}</th>
                        <td class="text-left">{$i['CDESCRI']}</td>
                        <td class="text-center">{$i['DINICIO']}</td>
                        <td class="text-center">{$i['DFINALI']}</td>
                        <td class="text-left">{$i['CNOMBRE']}</td>
                        <td class="align-middle text-center p-0"><button type="button" value="{$k}" tabindex="-1"><img src="css/svg/edit-blue.svg" width="19" height="18"></button></td>
                        <td class="align-middle text-center p-0"><button type="button" value="{$k}" tabindex="-1"><img src="css/svg/x-red.svg" width="19" height="18"></button></td>
                     </tr>
                  {/foreach}
               {/if}
            </tbody>
         </table>
      </div>
      <div class="input-group input-group-sm mb-3 justify-content-center">
         <div class="btn-group btn-group-sm" role="group" style="margin-top: 1px;">
            <button type="button" class="btn btn-outline-primary" data-toggle="modal" data-target="#modal_agregarTarea">Agregar Tarea</button>
         </div>
      </div>
      <div class="form-group text-15 mb-1">
         <label class="mb-1">6. PRESUPUESTO DETALLADO DE RECURSOS NECESARIOS PARA EL DESARROLLO DE LA ACTIVIDAD EN FUNCIÓN AL RESULTADO PREVISTO</label>
      </div>
      <div class="table-responsive mh-40 mb-0">
         <table class="table table-sm table-hover text-12 table-collapse mb-0">
            <thead class="bg-coral-1">
               <tr class="text-center py-0">
                  <th class="align-middle py-1" scope="row" style="width: 2%">#</th>
                  <th class="align-middle py-1" scope="row" style="width: 60%">ARTÍCULO / CONCEPTO</th>
                  <th class="align-middle py-1" scope="row" style="width: 15%">UNIDAD DE MEDIDA</th>
                  <th class="align-middle py-1" scope="row" style="width: 6%">P. UNITARIO</th>
                  <th class="align-middle py-1" scope="row" style="width: 5%">CANTIDAD</th>
                  <th class="align-middle py-1" scope="row" style="width: 8%">VALOR TOTAL</th>
                  <th class="align-middle py-1" scope="row" style="width: 2%"><img src="css/svg/edit-blue.svg" width="15" height="15"></th>
                  <th class="align-middle py-1" scope="row" style="width: 2%"><img src="css/svg/x-red.svg" width="15" height="15"></th>
               </tr>
            </thead>
            <tbody id="detalleArticulos" class="text-12">
               <tr>
                  <th scope="row" class="text-right">999</th>
                  <td class="text-left">ARTICULO 1 ARTICULO 2 ARTICULO 3 ETC ARTICULO 1 ARTICULO 2 ARTICULO 3 ETC ETC ARTICULO 1 ARTICULO 2 ARTICULO 3 ETC ETC</td>
                  <td class="text-center">UNIDAD UNIDAD UNIDAD UNIDAD</td>
                  <td class="text-right">9,999,999.00</td>
                  <td class="text-right">99,999.00</td>
                  <td class="text-right">9,999,999,999.00</td>
                  <td class="align-middle text-center p-0"><button type="button" value="{$k}" tabindex="-1"><img src="css/svg/edit-blue.svg" width="19" height="18"></button></td>
                  <td class="align-middle text-center p-0"><button type="button" value="{$k}" tabindex="-1"><img src="css/svg/x-red.svg" width="19" height="18"></button></td>
               </tr>
               {$k = 0}
               {foreach from=$saDatos item=i}
                  <tr>
                     <th scope="row" class="text-right">{$k+1}</th>
                     <td class="text-left">{$i['CDESCRI']}</td>
                     <td class="text-center">{$i['DINICIO']}</td>
                     <td class="text-center">{$i['DFINALI']}</td>
                     <td class="text-left">{$i['CCODUSU']}</td>
                     <td class="align-middle text-center p-0"><button type="button" value="{$k}" tabindex="-1"><img src="css/svg/edit-blue.svg" width="19" height="18"></button></td>
                     <td class="align-middle text-center p-0"><button type="button" value="{$k}" tabindex="-1"><img src="css/svg/x-red.svg" width="19" height="18"></button></td>
                  </tr>
               {/foreach}
            </tbody>
         </table>
      </div>
      <div class="input-group input-group-sm mb-3 justify-content-center">
         <div class="btn-group btn-group-sm" role="group" style="margin-top: 1px;">
            <button type="button" class="btn btn-outline-primary">Útiles de Escritorio</button>
            <button type="button" class="btn btn-outline-primary">Suministros de Computo</button>
            <button type="button" class="btn btn-outline-primary">Limpieza</button>
            <button type="button" class="btn btn-outline-primary">Infraestructura</button>
            <button type="button" class="btn btn-outline-primary">Otros</button>
         </div>
      </div>
      <div class="input-group input-group-sm mb-3 justify-content-center">
         <button type="submit" name="Boton1" value="Grabar" class="btn bg-ucsm col-lg-3 mx-2" onclick="return confirm('¿Desea crear/editar esta actividad?\nLa actividad puede ser editada/anulada posteriormente.');">GRABAR</button>
         <button type="submit" name="Boton1" value="Cancelar" class="btn btn-danger col-lg-3 mx-2" formnovalidate>CANCELAR</button>
      </div>
   {/if}
</div>
</form>
</body>
<div class="modal p-0" id="modal_agregarTarea" tabindex="-1" role="dialog">
   <div class="modal-dialog" role="document" style="max-width: 90%!important;">
      <div class="modal-content">
         <div class="modal-header">
            <h5 class="modal-title">AGREGAR TAREA</h5>
            <button type="button" class="close" data-dismiss="modal">
               <span aria-hidden="true">&times;</span>
            </button>
         </div>
         <div class="modal-body">
            <input type="hidden" id="modal_agregarTarea_nIndice" value="0">
            <div class="input-group input-group-sm mb-1 justify-content-center">
               <div class="input-group-prepend col-lg-2 px-0"><span class="input-group-text w-100">DESCRIPCIÓN</span></div>
               <input type="text" id="modal_agregarTarea_cDescri" class="form-control text-uppercase" placeholder="DESCRIPCIÓN DE LA TAREA">
            </div>
            <div class="input-group input-group-sm mb-1 justify-content-center">
               <div class="input-group-prepend col-lg-2 px-0"><span class="input-group-text w-100">INICIO</span></div>
               <input type="text" id="modal_agregarTarea_dInicio" class="form-control text-center text-uppercase" placeholder="aaaa-mm-dd">
               <div class="input-group-prepend col-lg-2 px-0"><span class="input-group-text w-100">FINALIZACIÓN</span></div>
               <input type="text" id="modal_agregarTarea_dFinali" class="form-control text-center text-uppercase" placeholder="aaaa-mm-dd">
            </div>
            <div class="input-group input-group-sm mb-1 justify-content-center">
               <div class="input-group-prepend col-lg-2 px-0"><span class="input-group-text w-100">RESPONSABLE</span></div>
               <input type="text" id="modal_agregarTarea_buscarCodUsu" class="form-control text-uppercase" placeholder="DNI / CÓDIGO TRABAJADOR / APELLIDOS Y NOMBRES">
               <div class="input-group-prepend col-lg-2 px-0"><button onclick="f_BuscarUsuario();" class="btn btn-sm btn-outline-secondary w-100" type="button">BUSCAR</button></div>
               <select id="modal_agregarTarea_cCodUsu" class="custom-select custom-select-sm col-lg-4">
                  <option>SELECCIONE UNA OPCIÓN ...</option>
               </select>
            </div>
         </div>
         <div class="modal-footer">
            <button type="button" class="btn btn-danger" data-dismiss="modal">Cerrar</button>
            <button type="button" class="btn btn-success" id="modal_agregarTarea_btnAgregarTarea" onclick="f_AgregarTarea();">AGREGAR TAREA</button>
         </div>
      </div>
   </div>
</div>
</html>